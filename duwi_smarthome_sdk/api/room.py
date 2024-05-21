import json
from typing import List, Optional

from duwi_smarthome_sdk.const.const import URL
from duwi_smarthome_sdk.const.status import Code
from duwi_smarthome_sdk.model.resp.room import RoomInfo
from duwi_smarthome_sdk.util.http import get
from duwi_smarthome_sdk.util.sign import md5_encrypt
from duwi_smarthome_sdk.util.timestamp import current_timestamp


class RoomInfoClient:
    def __init__(self,
                 app_key: str,
                 app_secret: str,
                 access_token: str,
                 app_version: str,
                 client_version: str,
                 client_model: Optional[str] = None
                 ):
        self._url = URL
        self._app_key = app_key
        self._app_secret = app_secret
        self._access_token = access_token
        self._app_version = app_version
        self._client_version = client_version
        self._client_model = client_model

    async def fetch_room_info(self, house_no: str) -> tuple[str, List[RoomInfo] | None]:
        body = {
            "houseNo": house_no
        }
        body_string = (((json.dumps(body, separators=(',', ':'))
                         .replace('{', ""))
                        .replace('}', "")
                        .replace(":", '=')
                        .replace(",", "&"))
                       .replace('"', ''))

        sign = md5_encrypt(body_string + self._app_secret + str(current_timestamp()))

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
        status, message, res = await get(URL + "/room/infos?houseNo=" + house_no, headers, {})

        if status == Code.SUCCESS.value:
            room_infos = res.get('rooms', [])
            room_info_objects = [self._create_room_info_obj(r_info) for r_info in room_infos]
            return status, room_info_objects

        return status, None

    @staticmethod
    def _create_room_info_obj(r_info: dict) -> RoomInfo:
        return RoomInfo(
            room_no=r_info.get('roomNo', ''),
            room_name=r_info.get('roomName', ''),
            house_no=r_info.get('houseNo', ''),
            floor_no=r_info.get('floorNo', ''),
            create_time=r_info.get('createTime', ''),
            seq=r_info.get('seq', 0),
            room_image=r_info.get('roomImage', '')
        )
