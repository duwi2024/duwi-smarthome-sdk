from types import SimpleNamespace
from typing import Any


class CustomerDevice(SimpleNamespace):
    def __init__(self, device_dict: dict[str, Any], _Logger=None, **kwargs: Any):
        super().__init__(**kwargs)
        self.device_no = device_dict.get("deviceNo", device_dict.get("deviceGroupNo", ""))
        self.device_name = device_dict.get("deviceName", device_dict.get("deviceGroupName", ""))
        self.device_type = device_dict.get("deviceType", "")
        self.terminal_sequence = device_dict.get("terminalSequence", "")
        self.host = device_dict.get("host", "")
        self.route_num = device_dict.get("routeNum", 0)
        self.device_type_no = device_dict.get("deviceTypeNo", "")
        self.device_sub_type_no = device_dict.get("deviceSubTypeNo", "")
        self.house_no = device_dict.get("houseNo", "")
        self.room_no = device_dict.get("roomNo", "")
        self.floor_no = device_dict.get("floorNo", "")
        self.room_name = device_dict.get("roomName", "")
        self.floor_name = device_dict.get("floorName", "")
        self.is_online = device_dict.get("isOnline", False)
        self.is_group = device_dict.get("isGroup", False)
        self.hosts = device_dict.get("syncHostSequences", []) if self.is_group else []
        self.create_time = device_dict.get("createTime", "")
        self.seq = device_dict.get("seq", 0)
        self.is_favorite = device_dict.get("isFavorite", 0)
        self.favorite_time = device_dict.get("favoriteTime", "")
        self.terminal_name = device_dict.get("terminalName", "")
        self.is_gesture_password = device_dict.get("isGesturePassword", False)
        self.icon = device_dict.get("icon", "")
        self.main_device_no = device_dict.get("mainDeviceNo", "")
        self.is_virtual_device = device_dict.get("isVirtualDevice", False)
        self.device_group_type = device_dict.get("deviceGroupType", "")
        self.execute_way = device_dict.get("executeWay", "")
        self.value = device_dict.get("value", {})
        self.is_follow_online = device_dict.get("isFollowOnline", False)
        if not self.is_group:
            self.value["online"] = self.is_online
        if not self.hosts:
            self.hosts = device_dict.get("hosts", [])

    def __eq__(self, other):
        """If devices are the same one."""
        return self.device_no == other.device_no


class CustomerScene(SimpleNamespace):
    def __init__(self, scene_dict: dict[str, Any], _Logger=None, **kwargs: Any):
        super().__init__(**kwargs)
        self.scene_no = scene_dict.get("sceneNo", "")
        self.scene_name = scene_dict.get("sceneName", "")
        self.room_no = scene_dict.get("roomNo", "")
        self.room_name = scene_dict.get("roomName", "")
        self.floor_no = scene_dict.get("floorNo", "")
        self.floor_name = scene_dict.get("floorName", "")
        self.house_no = scene_dict.get("houseNo", "")
        self.execute_way = scene_dict.get("executeWay", 0)
        self.sync_host_sequences = scene_dict.get("syncHostSequences", [])
