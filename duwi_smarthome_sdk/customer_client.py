from typing import Optional, Any

from .base_api import CustomerApi
from .device_control import ControlDevice


class CustomerClient:
    def __init__(self, client: CustomerApi):
        self._client = client

    async def login(self, phone: str, password: str) -> dict[str, Any] | None:
        return await self._client.post("/account/login", None, {
            "phone": phone,
            "password": password,
        })

    async def control(self, is_group: bool, body: Optional[ControlDevice]) -> dict[str, Any] | None:
        endpoint = "/deviceGroup/batchCommandOperate" if is_group else "/device/batchCommandOperate"
        return await self._client.post(endpoint, None, body.to_dict() if body else None)

    async def discover(self) -> dict[str, Any]:
        return await self._client.get("/device/infos", {"houseNo": self._client.house_no})

    async def fetch_floor_info(self) -> dict[str, Any] | None:
        return await self._client.get("/floor/infos", {"houseNo": self._client.house_no})

    async def fetch_house_info(self) -> dict[str, Any] | None:
        return await self._client.get("/house/infos")

    async def discover_groups(self) -> dict[str, Any]:
        return await self._client.get("/deviceGroup/infos", {"houseNo": self._client.house_no})

    async def refresh(self) -> dict[str, Any] | None:
        return await self._client.put("/account/token", {"refreshToken": self._client.refresh_token})

    async def fetch_room_info(self) -> dict[str, Any] | None:
        return await self._client.get(f"/room/infos", {"houseNo": self._client.house_no})

    async def control_scene(self, sceneNo: str) -> dict[str, Any] | None:
        return await self._client.post("/scene/execute", None, {
            "houseNo": self._client.house_no,
            "sceneNo": sceneNo
        })

    async def fetch_terminal_info(self) -> dict[str, Any] | None:
        return await self._client.get("/terminal/infos", {"houseNo": self._client.house_no})

    async def fetch_scene_info(self) -> dict[str, Any] | None:
        return await self._client.get("/scene/infos", {"houseNo": self._client.house_no})
