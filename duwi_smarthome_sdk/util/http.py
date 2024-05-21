from typing import Any, Dict, Optional, Tuple
import aiohttp


async def _create_session() -> aiohttp.ClientSession:
    return aiohttp.ClientSession()


async def get(
        url: str,
        headers: Optional[Dict[str, str]] = None,
        query: Optional[Dict[str, str]] = None
) -> Tuple[str, str, Any | None]:
    return await _request("GET", url, headers=headers, params=query)


async def post(
        url: str,
        headers: Optional[Dict[str, str]] = None,
        body: Optional[Dict[str, Any]] = None
) -> Tuple[str, str, Any | None]:
    return await _request("POST", url, headers=headers, json=body)


async def put(
        url: str,
        headers: Optional[Dict[str, str]] = None,
        body: Optional[Dict[str, Any]] = None
) -> Tuple[str, str, Any | None]:
    return await _request("PUT", url, headers=headers, json=body)


async def delete(
        url: str,
        headers: Optional[Dict[str, str]] = None,
        query: Optional[Dict[str, str]] = None
) -> Tuple[str, str, Any | None]:
    return await _request("DELETE", url, headers=headers, params=query)


async def _request(
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None
) -> Tuple[str, str, Any | None]:
    session = await _create_session()
    try:
        async with session.request(method=method, url=url, headers=headers, params=params, json=json) as response:
            response_data = await response.json()
            return str(response_data.get("code")), response_data.get("message"), response_data.get("data")
    except aiohttp.ClientError as e:
        return "SysError", 'system error', {'error': str(e)}
    finally:
        await session.close()
