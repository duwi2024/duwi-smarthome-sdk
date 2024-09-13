# Duwi Device Management SDK

A Python SDK for Duwi Open API, which provides basic IoT capabilities like device management capabilities, helping you create IoT solutions. The Duwi IoT Development Platform opens basic IoT capabilities such as device management and data analytics services, helping you build robust IoT applications.

## Features

### APIs

- Manager.customerClient
  - `login(phone: str, password: str) -> dict[str, Any] | None`
  - `control(is_group: bool, body: Optional[ControlDevice]) -> dict[str, Any] | None`
  - `discover() -> dict[str, Any]`
  - `fetch_floor_info() -> dict[str, Any] | None`
  - `fetch_house_info() -> dict[str, Any] | None`
  - `discover_groups() -> dict[str, Any]`
  - `refresh() -> dict[str, Any] | None`
  - `fetch_room_info() -> dict[str, Any] | None`
  - `control_scene(sceneNo: str) -> dict[str, Any] | None`
  - `fetch_terminal_info() -> dict[str, Any] | None`
  - `fetch_scene_info() -> dict[str, Any] | None`

### Device Listeners

- `SharingDeviceListener`: Interface for listening to device state changes.
- `SharingTokenListener`: Interface for handling authentication token updates.

## Possible Scenarios

- Smart Home Integration
- Automated Device Control
- Real-time Device Monitoring

## Usage

### Installation

```bash
pip3 install duwi-open-sdk
```

### Example

#### Initialize the Manager

To initialize the manager, use the following code:

```python
from duwi_smarthome_sdk.device_scene_models import CustomerDevice
from duwi_smarthome_sdk import Manager

manager = Manager(
    _id="example_entry_id",
    customer_api=CustomerApi(
        address=HTTP_ADDRESS,
        ws_address=WEBSOCKET_ADDRESS,
        app_key="your_app_key",
        app_secret="your_app_secret",
        house_no="your_house_no",
        house_name="Your House Name",
        access_token="your_access_token",
        refresh_token="your_refresh_token",
        client_version="1.0",
        client_model="Model XYZ",
        app_version="0.1.0",
    ),
    house_key="your_house_key",
)

# Execute login
login_status = await manager.login("your_phone_number", "your_password")
```

### Implementing Listeners

To listen to device status updates and handle token authentication, implement the listeners as follows:

```python
class DeviceListener(SharingDeviceListener):
    async def on_device_update(self, device_id: str, data: dict):
        # Handle device update logic
        pass

class TokenListener(SharingTokenListener):
    async def on_token_refresh(self, new_token: str):
        # Handle token refresh logic
        pass
    
# Add the listeners to the manager
device_listener = DeviceListener()
token_listener = TokenListener()

manager.add_device_listener(device_listener)
```

### Accessing Device Information

You can access any device information through the manager:

```python
device_info = manager.device_map.get("your_device_id")
```

## Release Note

| version | Description       |
|---------|-------------------|
| 0.7.1   | Initial release    |

## Issue Feedback

You can provide feedback on your issue via **Github Issue**.

## License

**duwi-device-management-sdk** is available under the MIT license. Please see the [LICENSE](./LICENSE) file for more info.
