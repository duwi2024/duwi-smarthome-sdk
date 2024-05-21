import json

from duwi_smarthome_sdk.const.const import URL
from duwi_smarthome_sdk.util.http import put
from duwi_smarthome_sdk.const.status import Code
from duwi_smarthome_sdk.util.sign import md5_encrypt
from duwi_smarthome_sdk.util.timestamp import current_timestamp
from duwi_smarthome_sdk.model.resp.auth import AuthToken


class AuthTokenRefresherClient:
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

    async def refresh(self, refresh_token: str) -> tuple[str, AuthToken | None]:
        body = {
            "refreshToken": refresh_token,
        }

        body_string = json.dumps(body, separators=(',', ':'))
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

        status, message, res = await put(self._url + "/account/token", headers, body)
        if status == Code.SUCCESS.value:
            return status, AuthToken(
                access_token=res.get("accessToken"),
                access_token_expire_time=res.get("accessTokenExpireTime"),
                refresh_token=res.get("refreshToken"),
                refresh_token_expire_time=res.get("refreshTokenExpireTime")
            )
        else:
            return status, None
