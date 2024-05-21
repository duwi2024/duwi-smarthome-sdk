import json
from typing import Optional

from duwi_smarthome_sdk.util.sign import md5_encrypt
from duwi_smarthome_sdk.util.timestamp import current_timestamp
from duwi_smarthome_sdk.const.const import URL
from duwi_smarthome_sdk.util.http import post
from duwi_smarthome_sdk.model.req.device_control import ControlDevice


class ControlClient:

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

    async def control(self, body: Optional[ControlDevice]) -> str:
        body_string = json.dumps(body.to_dict(), separators=(',', ':')) if body else ""

        sign = md5_encrypt(f"{body_string}{self._app_secret}{current_timestamp()}")

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

        body_dict = body.to_dict() if body else None

        status, message, res = await post(f"{self._url}/device/batchCommandOperate", headers, body_dict)

        return status
