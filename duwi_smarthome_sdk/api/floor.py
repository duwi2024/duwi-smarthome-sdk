from duwi_smarthome_sdk.model.resp.floor import FloorInfo
from duwi_smarthome_sdk.const.status import Code
from duwi_smarthome_sdk.const.const import URL
from duwi_smarthome_sdk.util.http import get
from duwi_smarthome_sdk.util.sign import md5_encrypt
from duwi_smarthome_sdk.util.timestamp import current_timestamp

import json
import logging

_LOGGER = logging.getLogger(__name__)


class FloorInfoClient:
    def __init__(self,
                 app_key: str,
                 app_secret: str,
                 access_token: str,
                 app_version: str,
                 client_version: str,
                 client_model: str = None
                 ):
        self._url = URL
        self._app_key = app_key
        self._app_secret = app_secret
        self._access_token = access_token
        self._app_version = app_version
        self._client_version = client_version
        self._client_model = client_model

    async def fetch_floor_info(self, house_no: str) -> tuple[str, list[FloorInfo] | None]:
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
            'time': str(current_timestamp()),
            'sign': sign,
            'appVersion': self._app_version,
            'clientVersion': self._client_version,
            'clientModel': self._client_model
        }
        status, message, res = await get(URL + "/floor/infos?houseNo=" + house_no, headers, {})

        if status == Code.SUCCESS.value:
            floor_infos = res.get('floors', [])
            floor_info_objects = [self._create_floor_info_obj(f_info) for f_info in floor_infos]
            return status, floor_info_objects

        return status, None

    @staticmethod
    def _create_floor_info_obj(f_info: dict) -> FloorInfo:
        return FloorInfo(
            floor_no=f_info.get('floorNo', ''),
            house_no=f_info.get('houseNo', ''),
            floor_name=f_info.get('floorName', ''),
            seq=f_info.get('seq', 0),
            create_time=f_info.get('createTime', '')
        )
