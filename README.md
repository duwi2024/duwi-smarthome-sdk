## Installation

First, you need to make sure you have the SDK installed in your environment. You can do this by running:

```shell
pip install duwi_smarthome_sdk_dev
```

To update the SDK or any existing dependencies to their latest versions, execute:

```shell
pip install --upgrade duwi_smarthome_sdk_dev
```

## Usage

### Authentication

Before you start fetching information or interacting with devices, you need to authenticate and obtain an access token. Start by initializing the login client:

```python
from duwi_smarthome_sdk_dev import AccountClient

cc = AccountClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    app_version="0.0.1",
    client_version="0.0.1",
    client_model="homeassistant",
)

res = await cc.login(phone="your_phone_number", password="your_password")
```

Once logged in, you will receive an access token. This token will be used in subsequent requests to authenticate and authorize your interactions.

### Fetching House Information

With the access token, you can now fetch house information or any other data provided by the SDK. Initialize the house info client with your credentials and access token:

```python
from duwi_smarthome_sdk_dev import HouseInfoClient

cc = HouseInfoClient(
    app_key="your_app_key",
    app_secret="your_app_secret",
    access_token="your_access_token",
    app_version="0.0.1",
    client_version="0.0.1",
    client_model="homeassistant",
)

res = await cc.fetch_house_info()
```

### WebSocket Device Synchronization

For real-time device synchronization, set up the WebSocket (WS) client with the necessary credentials. You will also need to define a callback function that handles incoming messages.

#### Setting up the WebSocket Client

```python
from duwi_smarthome_sdk_dev import DeviceSynchronizationWS
import logging

_LOGGER = logging.getLogger(__name__)

# Define your callback function
async def on_callback(message: str):
    _LOGGER.info(f"on_callback: {message}")

# Initialize the WS client with your credentials
ws = DeviceSynchronizationWS(
    on_callback=on_callback,
    app_key="your_app_key",
    app_secret="your_app_secret",
    access_token="your_access_token",
    refresh_token="your_refresh_token",
    house_no="your_house_no",
    app_version="0.0.1",
    client_version="0.0.1",
    client_model="homeassistant",
)

_LOGGER.warning('Connecting to WS server...')
await ws.reconnect()
await ws.listen()
await ws.keep_alive()
```

This will establish a connection to the WebSocket server, listen for messages, and handle them using the provided callback function.

## Conclusion

By following these steps, you should have a functional setup allowing you to authenticate, fetch data, and synchronize devices in real-time using the `duwi_smarthome_sdk_dev`. This guide should serve as a starting point for integrating your smart home devices with Home Assistant using the SDK.