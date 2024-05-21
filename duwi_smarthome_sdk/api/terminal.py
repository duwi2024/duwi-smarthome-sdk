import json
from typing import List, Optional

from duwi_smarthome_sdk.const.const import URL
from duwi_smarthome_sdk.const.status import Code
from duwi_smarthome_sdk.model.resp.terminal import TerminalInfo
from duwi_smarthome_sdk.util.http import get
from duwi_smarthome_sdk.util.sign import md5_encrypt
from duwi_smarthome_sdk.util.timestamp import current_timestamp

class TerminalClient:
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

    async def fetch_terminal_info(self, house_no: str) -> tuple[str, List[TerminalInfo] | None]:
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
        status, message, res = await get(URL + "/terminal/infos?houseNo=" + house_no, headers, {})

        if status == Code.SUCCESS.value:
            terminal_infos = res.get('terminals', [])
            terminal_objects = [self._create_terminal_obj(t_info) for t_info in terminal_infos]
            return status, terminal_objects

        return status, None

    @staticmethod
    def _create_terminal_obj(t_info: dict) -> TerminalInfo:
        return TerminalInfo(
            terminal_name=t_info.get('terminalName', ''),
            terminal_sequence=t_info.get('terminalSequence', ''),
            short_code=t_info.get('shortCode', ''),
            product_model=t_info.get('productModel', ''),
            product_logo=t_info.get('productLogo', ''),
            seq=t_info.get('seq', 0),
            is_gateway=t_info.get('isGateWay', 0),
            host_sequence=t_info.get('hostSequence', ''),
            create_time=t_info.get('createTime', ''),
            product_show_model=t_info.get('productShowModel', ''),
            is_follow_online=t_info.get('isFollowOnline', False),
            is_online=t_info.get('isOnline', False)
        )

