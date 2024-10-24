import asyncio
import json
import time
from abc import ABCMeta
from typing import Any

import aiohttp
from aiohttp import ClientTimeout

from .const import DuwiCode
from .sign import md5_encrypt

from .const import _LOGGER


class CustomerApi:
    def __init__(
            self,
            address: str,
            ws_address: str,
            app_key: str,
            app_secret: str,
            app_version: str,
            client_version: str,
            client_model: str,
            house_no: str = "",
            access_token: str = "",
            refresh_token: str = "",
    ):
        self.address = address
        self.ws_address = ws_address
        self.house_no = house_no
        self.app_key = app_key
        self.app_secret = app_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.app_version = app_version
        self.client_version = client_version
        self.client_model = client_model
        self.timeout = ClientTimeout(total=15)
        self.access_token_expire_time = None

    def __generate_headers(self, method: str, body: dict[str, Any] | str) -> dict[str, str]:
        if body is None:
            body = {}

        if method == "GET":
            sorted_params = sorted(body.items())
            body_string = "&".join(f"{k}={v}" for k, v in sorted_params)
            body_string = body_string.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")
        else:
            body_string = json.dumps(body, separators=(',', ':'))

        timestamp = int(time.time() * 1000)
        sign = md5_encrypt(body_string + self.app_secret + str(timestamp))
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_token,
            'appkey': self.app_key,
            'time': str(timestamp),
            'sign': sign,
            'appVersion': self.app_version,
            'clientVersion': self.client_version,
            'clientModel': self.client_model,
        }
        return headers

    async def __request(
            self,
            method: str,
            path: str,
            params: dict[str, Any] | None = None,
            body: dict[str, Any] = None,
            retries: int = 3,
            backoff_factor: float = 0.3
    ) -> dict[str, Any] | None:
        headers = self.__generate_headers(method, params if method == "GET" else body)
        session = aiohttp.ClientSession(timeout=self.timeout)

        for attempt in range(retries):
            try:
                async with session.request(method=method, url=self.address + path, headers=headers, params=params,
                                           json=body) as response:
                    response_data = await response.json()
                    if isinstance(response_data, dict):
                        return response_data
                    else:
                        _LOGGER.error("Unexpected response format: not a dictionary")
                        return {"code": DuwiCode.SYS_ERROR.value}
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                _LOGGER.warning(f"Request failed: {e}. Attempt {attempt + 1}/{retries}.")
                if attempt == retries - 1:
                    return {"code": DuwiCode.SYS_ERROR.value}

                await asyncio.sleep(backoff_factor * (2 ** attempt))
            finally:
                await session.close()

    async def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        return await self.__request("GET", path, params, None)

    async def post(self, path: str, params: dict[str, Any] | None = None, body: dict[str, Any] | None = None) -> dict[
        str, Any]:
        return await self.__request("POST", path, params, body)

    async def put(self, path: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
        return await self.__request("PUT", path, None, body)

    async def delete(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        return await self.__request("DELETE", path, params, None)
