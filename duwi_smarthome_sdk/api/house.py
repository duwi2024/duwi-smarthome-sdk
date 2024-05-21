from duwi_smarthome_sdk.model.resp.house import HouseInfo
from duwi_smarthome_sdk.const.status import Code
from duwi_smarthome_sdk.const.const import URL
from duwi_smarthome_sdk.util.http import get
from duwi_smarthome_sdk.util.sign import md5_encrypt
from duwi_smarthome_sdk.util.timestamp import current_timestamp

import json
import logging

_LOGGER = logging.getLogger(__name__)


class HouseInfoClient:
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

    async def fetch_house_info(self) -> tuple[str, list[HouseInfo] | None]:
        body = {}
        body_string = json.dumps(body, separators=(',', ':'))
        sign = md5_encrypt("" + self._app_secret + str(current_timestamp()))

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
        status, message, res = await get(URL + "/house/infos", headers, body)

        if status == Code.SUCCESS.value:
            house_infos = res.get('houseInfos', [])
            house_info_objects = [self._create_house_info_obj(h_info) for h_info in house_infos]
            return status, house_info_objects

        return status, None

    @staticmethod
    def _create_house_info_obj(h_info: dict) -> HouseInfo:
        return HouseInfo(
            house_no=h_info.get('houseNo', ''),
            house_name=h_info.get('houseName', ''),
            house_image_url=h_info.get('houseImageUrl'),
            address=h_info.get('address', ''),
            location=h_info.get('location', ''),
            seq=h_info.get('seq', 0),
            create_time=h_info.get('createTime', ''),
            deliver_time=h_info.get('deliverTime', ''),
            host_count=h_info.get('hostCount', 0),
            device_count=h_info.get('deviceCount', 0),
            lan_secret_key=h_info.get('lanSecretKey', '')
        )
