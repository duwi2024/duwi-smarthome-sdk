import json
import logging

from typing import Optional, List

from duwi_smarthome_sdk.model.resp.group import Group
from duwi_smarthome_sdk.util.http import get
from duwi_smarthome_sdk.const.status import Code
from duwi_smarthome_sdk.const.const import URL
from duwi_smarthome_sdk.util.sign import md5_encrypt
from duwi_smarthome_sdk.util.timestamp import current_timestamp

_LOGGER = logging.getLogger(__name__)


class GroupClient:
    """
    Client for discovering device groups registered under a specific house number through the Duwi's cloud service.
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
        Initializes the group client with the necessary authentication details.

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

    async def discover_groups(self, house_no: str) -> tuple[str, Optional[List[Group]]]:
        """
        Retrieves a list of device groups associated with the specified house number.

        :param house_no: The house number for which to retrieve device groups.
        :return: A tuple containing the status of the operation and a list of Group objects, or None if unsuccessful.
        """
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

        status, message, res = await get(f"{self._url}/deviceGroup/infos?houseNo={house_no}", headers, body)

        if status == Code.SUCCESS.value:
            groups = res.get("deviceGroups", [])
            group_objects = [self._create_group_obj(group) for group in groups]
            return status, group_objects
        else:
            return status, None

    @staticmethod
    def _create_group_obj(group_dict: dict) -> Group:
        """
        Converts a dictionary representing a device group into a Group object.

        :param group_dict: A dictionary containing device group details.
        :return: A Group object.
        """
        return Group(
            device_group_no=group_dict.get("deviceGroupNo"),
            device_group_name=group_dict.get("deviceGroupName", ""),
            house_no=group_dict.get("houseNo", ""),
            room_no=group_dict.get("roomNo", ""),
            icon=group_dict.get("icon", ""),
            is_favorite=group_dict.get("isFavorite"),
            favorite_time=group_dict.get("favoriteTime", ""),
            create_time=group_dict.get("createTime", ""),
            update_time=group_dict.get("updateTime", ""),
            execute_way=group_dict.get("executeWay"),
            device_group_type=group_dict.get("deviceGroupType", "").lower(),
            seq=group_dict.get("seq"),
            value=group_dict.get("value"),
            sync_host_sequences=group_dict.get("syncHostSequences", []),
            device_no=group_dict.get("deviceGroupNo", ""),
            device_name=group_dict.get("deviceGroupName", ""),
            terminal_sequence=group_dict.get("terminalSequence", ""),
            route_num=group_dict.get("routeNum"),
            device_type_no=group_dict.get("deviceTypeNo", ""),
            device_sub_type_no=group_dict.get("deviceSubTypeNo", ""),
            room_name=group_dict.get("roomName", ""),
            floor_no=group_dict.get("floorNo", ""),
            floor_name=group_dict.get("floorName", ""),
            is_use=group_dict.get("isUse"),
            is_online=group_dict.get("isOnline"),
            create_time_device=group_dict.get("createTimeDevice", ""),
            seq_device=group_dict.get("seqDevice"),
            is_favorite_device=group_dict.get("isFavoriteDevice"),
            favorite_time_device=group_dict.get("favoriteTimeDevice", ""),
            key_binding_quantity=group_dict.get("keyBindingQuantity"),
            key_mapping_quantity=group_dict.get("keyMappingQuantity"),
            value_device=group_dict.get("valueDevice")
        )


