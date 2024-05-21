import json
import logging

from typing import Optional
from typing import List

from duwi_smarthome_sdk.model.resp.device import Device
from duwi_smarthome_sdk.util.http import get
from duwi_smarthome_sdk.const.status import Code
from duwi_smarthome_sdk.const.const import URL
from duwi_smarthome_sdk.util.sign import md5_encrypt
from duwi_smarthome_sdk.util.timestamp import current_timestamp

_LOGGER = logging.getLogger(__name__)


class DiscoverClient:
    """
    Client for discovering devices registered under a specific house number through the Duwi's cloud service.
    """

    def __init__(self,
                 app_key: str,
                 app_secret: str,
                 access_token: str,
                 app_version: str,
                 client_version: str,
                 client_model: str = None
                 ):
        """
        Initializes the discover client with the necessary authentication details.

        :param app_key: The application key for SDK authentication.
        :param app_secret: The application secret for SDK authentication.
        """
        self._url = URL
        self._app_key = app_key
        self._app_secret = app_secret
        self._access_token = access_token
        self._app_version = app_version
        self._client_version = client_version
        self._client_model = client_model

    async def discover(self, house_no: str) -> tuple[str, Optional[List[Device]]]:
        """
        Retrieves a list of devices associated with the specified house number.

        :param access_token: The access token for interacting with the cloud service.
        :param house_no: The house number for which to discover devices.
        :return: A tuple containing the status of the operation and a list of Device objects, or None if unsuccessful.
        """
        # status, message, res

        body = {}
        body_string = json.dumps(body, separators=(',', ':'))

        # Generate a signature using the body string, app secret, and the current timestamp.
        sign = md5_encrypt(f"houseNo={house_no}{self._app_secret}{current_timestamp()}")

        headers = {
            'Content-Type': 'application/json',
            'accessToken': self._access_token,
            'appkey': self._app_key,
            'secret': self._app_secret,
            'time': str(current_timestamp()),  # Ensure it's converted to string
            'sign': sign,
            'appVersion': self._app_version,
            'clientVersion': self._client_version,
            'clientModel': self._client_model
        }

        status, message, res = await get(f"{self._url}/device/infos?houseNo={house_no}", headers, body)

        if status == Code.SUCCESS.value:
            devices = res.get("devices", [])
            devices_objects = [self._create_device_obj(device) for device in devices]
            return status, devices_objects
        else:
            return status, None

    @staticmethod
    def _create_device_obj(device_dict: dict) -> Device:
        """
        Converts a dictionary representing a device into a Device object.

        :param device_dict: A dictionary containing device details.
        :return: A Device object.
        """
        return Device(
            device_no=device_dict.get("deviceNo", ""),
            device_name=device_dict.get("deviceName", ""),
            terminal_sequence=device_dict.get("terminalSequence", ""),
            route_num=device_dict.get("routeNum", 0),
            device_type_no=device_dict.get("deviceTypeNo", ""),
            device_sub_type_no=device_dict.get("deviceSubTypeNo", ""),
            house_no=device_dict.get("houseNo", ""),
            room_no=device_dict.get("roomNo", ""),
            room_name=device_dict.get("roomName", ""),
            floor_no=device_dict.get("floorNo", ""),
            floor_name=device_dict.get("floorName", ""),
            is_use=device_dict.get("isUse", False),
            is_online=device_dict.get("isOnline", False),
            create_time=device_dict.get("createTime", ""),
            seq=device_dict.get("seq", 0),
            is_favorite=device_dict.get("isFavorite", False),
            favorite_time=device_dict.get("favoriteTime", ""),
            key_binding_quantity=device_dict.get("keyBindingQuantity", 0),
            key_mapping_quantity=device_dict.get("keyMappingQuantity", 0),
            value=device_dict.get("value", {})
        )
