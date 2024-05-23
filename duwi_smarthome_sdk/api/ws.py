import asyncio
import json
import logging
import traceback

import websockets

from duwi_smarthome_sdk.const.status import Code
from duwi_smarthome_sdk.api.refresh_token import AuthTokenRefresherClient
from duwi_smarthome_sdk.const.const import WS_URL
from duwi_smarthome_sdk.util.sign import md5_encrypt, sha256_base64
from duwi_smarthome_sdk.util.timestamp import current_timestamp

_LOGGER = logging.getLogger(__name__)


class DeviceSynchronizationWS:
    def __init__(self,
                 on_callback: callable,
                 app_key: str,
                 app_secret: str,
                 access_token: str,
                 refresh_token: str,
                 house_no: str,
                 app_version: str,
                 client_version: str,
                 client_model=None
                 ):
        self._on_callback = on_callback
        self._server_uri = WS_URL
        self._app_key = app_key
        self._app_secret = app_secret
        self._access_token = access_token
        self._refresh_token = refresh_token
        self._house_no = house_no
        self._app_version = app_version
        self._client_version = client_version
        self._client_model = client_model
        self._is_over = False
        self._connection = None

    async def connect(self):
        _LOGGER.info('connect ws server...')
        self._connection = await websockets.connect(self._server_uri)

    async def send(self, message):
        if self._connection:
            # _LOGGER.info('send message: %s', message)
            await self._connection.send(message)

    async def disconnect(self):
        if self._connection:
            _LOGGER.info('disconnect ws server...')
            await self._connection.close()

    async def reconnect(self):
        _LOGGER.info('reconnect ws server...')
        if self._is_over:
            return
        await self.connect()
        await self.link()
        await self.bind()

    async def listen(self):
        while True:
            try:
                if self._is_over:
                    return
                await self.process_messages()
            except websockets.exceptions.ConnectionClosedError:
                _LOGGER.info('listen ws connection closed, trying to reconnect...')
                await self.reconnect()
                await asyncio.sleep(5)
            except Exception as e:
                _LOGGER.error(f'An error occurred during listen: {e}')

    async def link(self):
        _LOGGER.info('link...')
        timestamp = current_timestamp()
        client_id = md5_encrypt(timestamp)

        data = {
            "clientID": client_id,
            "appKey": self._app_key,
            "time": str(current_timestamp()),
            "sign": sha256_base64(client_id, self._app_key, timestamp, self._app_secret),
        }
        json_string = json.dumps(data)
        await self.send(
            'LINK|' + json_string
        )

    async def bind(self):
        _LOGGER.info('bind...')
        data = {
            "accessToken": self._access_token,
            "houseNo": self._house_no,
        }
        json_string = json.dumps(data)
        await self.send(
            'BIND|' + json_string
        )

    async def refresh_token(self):
        auth = AuthTokenRefresherClient(
            app_key=self._app_key,
            app_secret=self._app_secret,
            access_token=self._access_token,
            app_version=self._app_version,
            client_version=self._client_version,
            client_model=self._client_model,
        )
        while True:
            if self._is_over:
                return
            status, token = await auth.refresh(
                refresh_token=self._refresh_token)
            if status == Code.SUCCESS.value:
                self._access_token = token.access_token
                self._refresh_token = token.refresh_token
            await asyncio.sleep(5 * 24 * 60 * 60)

    async def keep_alive(self):
        while True:
            try:
                if self._is_over:
                    return
                await self.send('KEEPALIVE')
                await asyncio.sleep(20)
            except websockets.exceptions.ConnectionClosedError:
                _LOGGER.info('keep_alive ws,connection closed, trying to reconnect...')
                await self.reconnect()
            except Exception as e:
                _LOGGER.error(f'An error occurred during keep_alive: {e}')

    async def process_messages(self):
        async for message in self._connection:
            try:
                if message == "KEEPALIVE":
                    continue
                _LOGGER.info(f"ws receive message:{message}")
                message = str.replace(message, "&excision&", "")
                await self._on_callback(message)
            except Exception as e:
                _LOGGER.error(f"error message detail: \n{traceback.format_exc()}")
