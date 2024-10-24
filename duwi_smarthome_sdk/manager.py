import json
import time
from abc import ABCMeta
from datetime import datetime
from typing import Any, List, Callable

from .const import _LOGGER, DuwiCode, HAVC_TYPE_MAP, DEVICE_TYPE_MAP, GROUP_TYPE
from .device_control import ControlDevice
from .device_scene_models import CustomerScene, CustomerDevice
from .base_api import CustomerApi
from .customer_client import CustomerClient
from .ws import DeviceSynchronizationWS


class SharingDeviceListener(metaclass=ABCMeta):
    """Sharing device listener."""

    @classmethod
    def update_device(cls, device: CustomerDevice):
        """Update device info.

        Args:
            device(CustomerDevice): updated device info
        """
        pass

    @classmethod
    def add_device(cls, device: CustomerDevice):
        """Device Added.

        Args:
            device(CustomerDevice): Device added
        """
        pass

    @classmethod
    def remove_device(cls, device_no: str):
        """Device removed.

        Args:
            device_no(str): device's id which removed
        """
        pass

    @classmethod
    def token_listener(cls, device_id: str):
        """Device removed.

        Args:
            device_id(str): device's id which removed
        """
        pass

    @classmethod
    def update_scene(cls, scene: CustomerScene):
        """Update device info.

        Args:
            scene(CustomerDevice): updated device info
        """
        pass


class Manager:
    def __init__(
            self,
            house_key: str,
            customer_api: CustomerApi,
            token_refresh_callback: Callable[[bool, [dict[str, Any]]], None]
    ) -> None:
        self._is_over = False
        self._customer_api = customer_api
        self.house_key = house_key
        self.device_map: dict[str, CustomerDevice] = {}
        self.scene_map: dict[str, CustomerScene] = {}
        self.host_list: List[str] = []
        self.customerClient = CustomerClient(self._customer_api)
        self.ws = DeviceSynchronizationWS(self._customer_api)
        self._token_refresh_callback = token_refresh_callback
        self._device_listeners = set()

    async def init_manager(self):
        refresh_data = await self.customerClient.refresh()
        if refresh_data.get("code") != DuwiCode.SUCCESS.value:
            _LOGGER.error("Duwi manager init failed.")
        else:
            self._customer_api.access_token_expire_time = refresh_data.get("data", {}).get("accessTokenExpireTime")
            _LOGGER.info("Duwi manager init success.")

    async def update_device_cache(self) -> bool:
        await self.ws.add_message_listener(self.on_ws_message)
        floor_data, room_data, terminal_data, terminal_cloud_dict = await self.init_from_cloud_data()
        if not floor_data or not room_data or not terminal_data or not terminal_cloud_dict:
            return False

        #
        host_sequence_list = []
        for key, value in terminal_cloud_dict.items():
            if (value.get("host") not in host_sequence_list and
                    (value.get("productModel") == 'DXH' or value.get("productModel") == "DXH-HMCUH743")):
                host_sequence_list.append(value.get("host"))

        self.host_list = host_sequence_list
        return True

    async def init_from_cloud_data(self):
        global floors_dict, rooms_floors_dict, rooms_dict, terminal_dict
        terminal_dict = {}
        device_data = await self.customerClient.discover()
        group_data = await self.customerClient.discover_groups()
        floor_data = await self.customerClient.fetch_floor_info()
        room_data = await self.customerClient.fetch_room_info()
        terminal_data = await self.customerClient.fetch_terminal_info()
        scene_data = await self.customerClient.fetch_scene_info()

        # 房间和楼层映射
        if floor_data.get("code") == DuwiCode.SUCCESS.value and room_data.get("code") == DuwiCode.SUCCESS.value:
            floors_dict = (
                {floor.get("floorNo"): floor.get("floorName") for floor in
                 floor_data.get("data", {}).get("floors", [])} if floor_data.get("data") else {}
            )
            rooms_floors_dict = (
                {room.get("roomNo"): room.get("floorNo") for room in
                 room_data.get("data", {}).get("rooms", [])} if room_data.get("data") else {}
            )
            rooms_dict = {room["roomNo"]: room["roomName"] for room in
                          room_data.get("data", {}).get("rooms", [])} if room_data.get("data") else {}
        else:
            _LOGGER.error("discover floor or room error")
            return floor_data, room_data, terminal_data, terminal_dict

        # 主机和从机映射 从机是否跟随上线
        if terminal_data.get("code") == DuwiCode.SUCCESS.value:
            terminal_dict = {terminal.get("terminalSequence"): {
                "host": terminal.get("hostSequence"),
                "isFollowOnline": terminal.get("isFollowOnline"),
                "productModel": terminal.get("productModel")
            } for terminal in
                terminal_data.get("data", {}).get("terminals", [])} if terminal_data.get("data") else {}
        else:
            _LOGGER.error("discover terminal error")
            return floor_data, room_data, terminal_data, terminal_dict

        # 跟新全局的设备或者群组属性
        if device_data is not None and device_data.get("code") == DuwiCode.SUCCESS.value:
            for device in device_data.get("data", {}).get("devices"):
                if device.get("isUse") == 0:
                    continue
                device["deviceType"] = DEVICE_TYPE_MAP.get(device.get("deviceSubTypeNo"))
                self.device_map[device.get("deviceNo")] = CustomerDevice(device)
        else:
            _LOGGER.error("discover device error")
            return floor_data, room_data, terminal_data, terminal_dict

        if group_data is not None and group_data.get("code") == DuwiCode.SUCCESS.value:
            for group in group_data.get("data", {}).get("deviceGroups"):
                group["isGroup"] = True
                group["deviceType"] = GROUP_TYPE.get(group.get("deviceGroupType"))
                self.device_map[group.get("deviceGroupNo")] = CustomerDevice(group)
        else:
            _LOGGER.error("discover group error")
            return floor_data, room_data, terminal_data, terminal_dict
        if scene_data is not None and scene_data.get("code") == DuwiCode.SUCCESS.value:
            for scene in scene_data.get("data", {}).get("scenes"):
                if not scene.get("isUse") or not scene.get("isManualExecute"):
                    continue
                self.scene_map[scene.get("sceneNo")] = CustomerScene(scene)
        else:
            _LOGGER.error("discover scene error")
            return floor_data, room_data, terminal_data, terminal_dict

        # 遍历设备设置设备的房间名和楼层名字
        for device in self.device_map.values():
            if device.room_no in rooms_floors_dict:
                device.room_name = rooms_dict.get(device.room_no)
                device.floor_no = rooms_floors_dict.get(device.room_no)
            if device.floor_no in floors_dict:
                device.floor_name = floors_dict.get(device.floor_no)
            if device.terminal_sequence in terminal_dict:
                device.hosts.append(terminal_dict.get(device.terminal_sequence).get("host"))
                device.is_follow_online = terminal_dict.get(device.terminal_sequence).get("isFollowOnline")
            if havc_data := HAVC_TYPE_MAP.get(device.device_sub_type_no):
                device.value["havc"] = havc_data

        # 遍历场景设置设备的房间名和楼层名字
        for scene in self.scene_map.values():
            if scene.room_no in rooms_floors_dict:
                scene.room_name = rooms_dict.get(scene.room_no)
                scene.floor_no = rooms_floors_dict.get(scene.room_no)
            if scene.floor_no in floors_dict:
                scene.floor_name = floors_dict.get(scene.floor_no)

        return floor_data, room_data, terminal_data, terminal_dict

    def on_ws_message(self, msg: str):
        """On message from websocket."""
        msg_dict = json.loads(msg)
        namespace = msg_dict.get("namespace")
        if namespace not in [
            "Duwi.RPS.DeviceValue",
            "Duwi.RPS.TerminalOnline",
            "Duwi.RPS.DeviceGroupValue",
        ]:
            _LOGGER.info(f"not support namespace: {msg_dict.get('namespace')}")
            return
        code_data = msg_dict.get("result", {}).get("msg")
        device_id = code_data.get("deviceNo") or code_data.get("deviceGroupNo")
        self._on_device_report(namespace, device_id, code_data)

    def _on_device_report(self, namespace: str, device_id: str, status: dict[str, Any]):
        if namespace == "Duwi.RPS.DeviceValue" or namespace == "Duwi.RPS.DeviceGroupValue":
            device = self.device_map.get(device_id, None)
            if not device:
                _LOGGER.warn(f"device {device_id} not found")
                return
            self.__update_device(device, status)
            if "device_use" in status:
                self.__change_device(device, status["device_use"])

        elif namespace == "Duwi.RPS.TerminalOnline":
            sequence = status.get("sequence")
            online = status.get("online")
            for d in self.device_map:
                device = self.device_map[d]
                if online:
                    if device.is_follow_online and device.terminal_sequence == sequence:
                        self.device_map[d].value["online"] = online
                        for listener in self._device_listeners:
                            listener.update_device(device)
                else:
                    if device.terminal_sequence == sequence or (sequence in device.hosts and len(device.hosts) == 1):
                        self.device_map[d].value["online"] = online
                        for listener in self._device_listeners:
                            listener.update_device(device)

    def __change_device(self, device: CustomerDevice, device_use: bool = False):
        """Change device status."""
        for listener in self._device_listeners:
            if device_use:
                listener.add_device(device)
            else:
                listener.remove_device(device.device_no)

    def __update_device(self, device: CustomerDevice, status: dict[str, Any]):
        """Update device status."""
        for k in status:
            device.value[k] = status[k]
        for listener in self._device_listeners:
            listener.update_device(device)

    def add_device_listener(self, listener: SharingDeviceListener):
        """Add device listener."""
        self._device_listeners.add(listener)

    def remove_device_listener(self, listener: SharingDeviceListener):
        """Remove device listener."""
        self._device_listeners.remove(listener)

    async def activate_scene(self, scene: CustomerScene):
        """Activate scene."""
        await self.customerClient.control_scene(scene.scene_no)

    async def send_commands(
            self, device_no: str, is_group: bool, commands: dict[str, Any]
    ):
        """Send commands."""
        cd = ControlDevice(
            device_no=device_no,
            house_no=self._customer_api.house_no,
            is_group=is_group
        )
        for k in commands:
            cd.add_param_info(k, commands[k])

        device = self.device_map.get(device_no, None)
        if not device:
            _LOGGER.warn(f"device {device_no} not found")
            return
        expire_time_str = self._customer_api.access_token_expire_time
        if expire_time_str:
            expire_time_dt = datetime.fromisoformat(expire_time_str)
            expire_time_ts = expire_time_dt.timestamp()
            if expire_time_ts < time.time() + 2 * 24 * 60 * 60:
                refresh_token_data = await self.customerClient.refresh()
                auth_data = refresh_token_data.get("data", {})
                # update token
                self._token_refresh_callback(
                    refresh_token_data.get("code") == DuwiCode.SUCCESS.value,
                    {
                        "access_token": auth_data.get("accessToken"),
                        "refresh_token": auth_data.get("refreshToken"),
                    },
                )
                self._customer_api.access_token_expire_time = auth_data.get(
                    "accessTokenExpire"
                )
        data = await self.customerClient.control(is_group, cd)
        if data.get("code") != DuwiCode.SUCCESS.value:
            _LOGGER.error("send_commands error = %s message %s", data.get("code"), data.get("message"))
        else:
            _LOGGER.info("send_commands success = %s message %s", data.get("code"), data.get("message"))

    async def unload(self, clear_local: bool = False):
        """Unload manager."""
        self._is_over = True
        await self.ws.remove_message_listener(self.on_ws_message)
        await self.ws.disconnect()
        if clear_local:
            self.device_map.clear()
