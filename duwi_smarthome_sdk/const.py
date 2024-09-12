import logging
from enum import Enum

_LOGGER = logging.getLogger(__package__)

# ADDRESS
HTTP_ADDRESS = "https://openapi.duwi.com.cn/homeApi/v1"
WEBSOCKET_ADDRESS = "wss://openws.duwi.com.cn:32013"


class DuwiCode(Enum):
    """Enumeration of error and status codes."""
    # Success
    SUCCESS = '10000'
    """Indicates a successful operation."""

    # System Error
    SYS_ERROR = '10001'
    """Indicates a system error occurred."""

    # Login Error
    LOGIN_ERROR = '11000'
    """Indicates an error with the account or password provided during login."""

    # App Key Error
    APP_KEY_ERROR = '99001'
    """Indicates an issue with the app key provided in the request."""

    # Signature Error
    SIGN_ERROR = '99002'
    """Indicates a signature validation error."""

    # Timestamp Timeout
    TIMESTAMP_TIMEOUT = '99003'
    """Indicates that the timestamp of the request has timed out."""

    # System Rate Limit
    SYSTEM_RATE_LIMIT = '99004'
    """Indicates that the system's rate limit has been exceeded."""

    # System Minute Rate Limit
    SYSTEM_MINUTE_RATE_LIMIT = '99005'
    """Indicates that the system's minute rate limit has been exceeded."""

    # System Hour Rate Limit
    SYSTEM_HOUR_RATE_LIMIT = '99006'
    """Indicates that the system's hour rate limit has been exceeded."""

    # Gateway System Error
    GATEWAY_SYS_ERROR = '99999'
    """Indicates a general error in the gateway system."""

    # Operation success
    OPERATION_SUCCESS = '10000'
    """Indicates that the operation was successful."""

    # App Key error
    OPERATION_APP_KEY_ERROR = '10001'
    """Indicates an error with the app key provided in the request."""

    # Signature error
    OPERATION_SIGN_ERROR = '10002'
    """Indicates a signature validation error."""

    # Timestamp timeout
    OPERATION_TIMESTAMP_TIMEOUT = '10003'
    """Indicates that the timestamp of the request has timed out."""

    # Parameter error
    OPERATION_PARAM_ERROR = '10004'
    """Indicates that there is an error with the parameters provided in the request."""

    # Access token error
    OPERATION_ACCESSTOKEN_ERROR = '10005'
    """Indicates an error related to the access token."""

    # Refresh token error
    OPERATION_REFRESHTOKEN_ERROR = '10006'
    """Indicates an error related to the refresh token."""

    # Data saving
    OPERATION_DATA_SAVING = '10007'
    """Indicates that data is currently being saved."""

    # Data exists
    OPERATION_DATA_EXISTS = '10008'
    """Indicates that the data already exists."""

    # Data not exists
    OPERATION_DATA_NOT_EXISTS = '10009'
    """Indicates that the requested data does not exist."""

    # Data error
    OPERATION_DATA_ERROR = '10010'
    """Indicates that there is an error with the data provided."""

    # Data save failed
    OPERATION_DATA_SAVE_FAILED = '10011'
    """Indicates that the attempt to save data has failed."""

    # Data query error
    OPERATION_DATA_QUERY_ERROR = '10012'
    """Indicates an error occurred while querying data."""

    # Associated data exists
    OPERATION_ASSOCIATED_DATA_EXISTS = '10013'
    """Indicates that associated data already exists."""

    # Operation failed
    OPERATION_FAILED = '10014'
    """Indicates that the operation has failed."""

    # No permission
    OPERATION_NO_PERMISSION = '10015'
    """Indicates that the user does not have permission to perform the operation."""

    # Not supported
    OPERATION_NOT_SUPPORTED = '10016'
    """Indicates that the operation is not supported."""

    # Timeout
    OPERATION_TIMEOUT = '10017'
    """Indicates that the operation has timed out."""

    # Business error
    OPERATION_BUSINESS_ERROR = '19997'
    """Indicates a general business logic error."""

    # Service error
    OPERATION_SERVICE_ERROR = '19998'
    """Indicates an error with the service."""

    # System error
    OPERATION_SYSTEM_ERROR = '19999'
    """Indicates a general system error."""

    # Login error
    ACCOUNT_LOGIN_ERROR = '11000'
    """Indicates an error during account login."""

    # Not registered
    ACCOUNT_NOT_REGISTERED = '11001'
    """Indicates that the account is not registered."""

    # Already registered
    ACCOUNT_ALREADY_REGISTERED = '11002'
    """Indicates that the account is already registered."""

    # Verified but no password change
    ACCOUNT_VERIFIED_NO_PASSWORD_CHANGE = '11003'
    """Indicates that the account is verified but the password cannot be changed."""

    # Not authorized
    ACCOUNT_NOT_AUTHORIZED = '11004'
    """Indicates that the account is not authorized to perform this action."""

    # Password error
    ACCOUNT_PASSWORD_ERROR = '11005'
    """Indicates that there is an error with the account password."""

    # Dealer not exists
    ACCOUNT_DEALER_NOT_EXISTS = '11006'
    """Indicates that the associated dealer does not exist."""

    # Untransferred house cannot be deleted
    ACCOUNT_UNTRANSFERRED_HOUSE_CANNOT_BE_DELETED = '11007'
    """Indicates that a house that has not been transferred cannot be deleted."""

    # QR code expired
    ACCOUNT_QR_EXPIRED = '11008'
    """Indicates that the QR code has expired."""

    # Login authorization code error
    ACCOUNT_LOGIN_AUTH_CODE_ERROR = '11009'
    """Indicates an error with the login authorization code."""

    # WeChat unauthorized
    ACCOUNT_WECHAT_UNAUTHORIZED = '11010'
    """Indicates that the WeChat account is not authorized."""

    # House not enable password
    ACCOUNT_HOUSE_NOT_ENABLE_PASSWORD = '11011'
    """Indicates that the house account does not have password enabled."""

    # Phone number unchangeable with untransferred house
    ACCOUNT_PHONE_NUMBER_UNCHANGEABLE_WITH_UNTRANSFERRED_HOUSE = '11012'
    """Indicates that the phone number cannot be changed while there is an untransferred house."""

    # Verification code error
    MESSAGE_VERIFICATION_CODE_ERROR = '12000'
    """Indicates an error with the verification code provided."""

    # Verification code expired
    MESSAGE_VERIFICATION_CODE_EXPIRED = '12001'
    """Indicates that the verification code has expired."""

    # House-related codes
    HOUSE_INFO_NOT_EXISTS = '13000'
    """Indicates that the house information does not exist."""

    HOUSE_NOT_AUTHORIZED = '13001'
    """Indicates that the house is not authorized for this action."""

    HOUSE_DELIVERED = '13006'
    """Indicates that the house has been delivered."""

    HOUSE_TRANSFERRED = '13007'
    """Indicates that the house has been transferred."""

    HOUSE_TRANSFER_ERROR = '13008'
    """Indicates that there was an error during the house transfer."""

    HOUSE_LOCATION_NOT_SET = '13019'
    """Indicates that the location of the house has not been set."""

    HOUSE_LOCATION_ENV_INFO_NOT_AVAILABLE = '13020'
    """Indicates that environmental information for the house location is not available."""

    # Floor-related codes
    FLOOR_INFO_NOT_EXISTS = '13002'
    """Indicates that the floor information does not exist."""

    FLOOR_INFO_EXISTS = '13003'
    """Indicates that the floor information exists."""

    FLOOR_HAS_ROOM = '13009'
    """Indicates that the floor has associated rooms."""

    FLOOR_NOT_AUTHORIZED = '13013'
    """Indicates that the floor is not authorized for this action."""

    # Room-related codes
    ROOM_INFO_NOT_EXISTS = '13004'
    """Indicates that the room information does not exist."""

    ROOM_INFO_EXISTS = '13005'
    """Indicates that the room information exists."""

    ROOM_NOT_AUTHORIZED = '13011'
    """Indicates that the room is not authorized for this action."""

    # Device and scene-related codes
    REMOVE_DEVICES_FROM_ROOM = '13010'
    """Indicates that devices are being removed from the room."""

    REMOVE_SCENES_FROM_ROOM = '13012'
    """Indicates that scenes are being removed from the room."""

    REMOVE_CONTROLLERS_FROM_HOUSE = '13014'
    """Indicates that controllers are being removed from the house."""

    REMOVE_GROUPS_FROM_ROOM = '13017'
    """Indicates that groups are being removed from the room."""

    # Vehicle-related codes
    UNBIND_VEHICLES_BEFORE_TRANSFER = '13018'
    """Indicates that vehicles must be unbound before transferring the house."""

    # Miscellaneous
    CANNOT_TRANSFER_TO_SELF = '13015'
    """Indicates that a transfer to oneself is not allowed."""

    IMAGE_NOT_EXISTS = '13016'
    """Indicates that the image does not exist."""

    # Controller addition and existence codes
    CONTROLLER_NOT_ADDED = '14000'
    """Indicates that the controller has not been added."""

    CONTROLLER_ALREADY_ADDED = '14002'
    """Indicates that the controller is already added."""

    CONTROLLER_NOT_IN_REPOSITORY = '14001'
    """Indicates that the controller is not present in the repository."""

    # Controller state codes
    CONTROLLER_OFFLINE = '14005'
    """Indicates that the controller is currently offline."""

    CONTROLLER_ONLINE = '14016'
    """Indicates that the controller is currently online."""

    CONTROLLER_NOT_AUTHORIZED = '14006'
    """Indicates that the controller is not authorized for this action."""

    # Master/slave controller management
    REMOVE_SLAVE_CONTROLLERS_FIRST = '14003'
    """Indicates that slave controllers must be removed before proceeding."""

    ONLY_ADD_MASTER_CONTROLLER = '14004'
    """Indicates that only a master controller can be added."""

    CONTROLLER_ALREADY_BOUND = '14017'
    """Indicates that the controller is already bound."""

    CONTROLLER_REPLACEMENT_NOT_ALLOWED = '14018'
    """Indicates that replacing this controller is not allowed."""

    # Network and configuration issues
    NETWORK_CONFIGURATION_NOT_SUPPORTED = '14007'
    """Indicates that the network configuration is not supported."""

    PROTOCOL_NOT_SUPPORTED = '14028'
    """Indicates that the specified protocol is not supported."""

    PROTOCOL_NOT_EXISTS = '14029'
    """Indicates that the specified protocol does not exist."""

    DIFFERENT_HOST_GATEWAY = '14032'
    """Indicates that a different host gateway is detected."""

    # Device and firmware issues
    DEVICE_NOT_MOUNTED = '14010'
    """Indicates that the device is not mounted."""

    DEVICE_TYPE_NOT_SUPPORTED = '14011'
    """Indicates that the device type is not supported."""

    FIRMWARE_VERSION_TOO_LOW = '14009'
    """Indicates that the firmware version is too low."""

    HOST_MEMORY_INSUFFICIENT = '14027'
    """Indicates that there is insufficient memory on the host."""

    # Replacement and synchronization processes
    CONTROLLER_DATA_SYNC_IN_PROGRESS = '14019'
    """Indicates that data synchronization for the controller is in progress."""

    CONTROLLER_REPLACEMENT_CONFIRMATION_IN_PROGRESS = '14020'
    """Indicates that confirmation for controller replacement is ongoing."""

    CONTROLLER_REPLACEMENT_FAILED = '14021'
    """Indicates that the controller replacement has failed."""

    CONTROLLER_REPLACEMENT_SUCCESS = '14023'
    """Indicates that the controller replacement was successful."""

    CONTROLLER_DEVICE_LIMIT_EXCEEDED = '14024'
    """Indicates that the limit of devices for the controller has been exceeded."""

    CONTROLLER_REMOTE_CONTROL_FAILED = '14025'
    """Indicates that remote control of the controller has failed."""

    # Ongoing operations
    ADDRESS_OPERATION_ALREADY_IN_PROGRESS = '14026'
    """Indicates that an address operation is already in progress."""

    CONTROLLER_DATA_COMPARISON_IN_PROGRESS = '14033'
    """Indicates that data comparison for the controller is currently in progress."""

    MAIN_CHANNEL_INFO_UPDATE_LIMIT = '14034'
    """Indicates that the update limit for main channel info has been reached."""

    LINE_SCANNING_IN_PROGRESS = '14035'
    """Indicates that line scanning is currently in progress."""

    LINE_SCANNING_FAILED = '14036'
    """Indicates that line scanning has failed."""

    # Product existence and type support codes
    PRODUCT_INFO_NOT_EXISTS = '15000'
    """Indicates that the product information does not exist."""

    MANUFACTURER_INFO_NOT_EXISTS = '15001'
    """Indicates that the manufacturer information does not exist."""

    PRODUCT_TYPE_NOT_SUPPORTED = '15002'
    """Indicates that the product type is not supported."""

    # Device existence and status codes
    DEVICE_NOT_EXISTS = '16001'
    """Indicates that the device does not exist."""

    DEVICE_DISABLED = '16003'
    """Indicates that the device is disabled."""

    DEVICE_OFFLINE = '16018'
    """Indicates that the device is currently offline."""

    DEVICE_HIDDEN = '16016'
    """Indicates that the device is hidden."""

    DEVICE_HIDDEN_IN_COMBINATION = '16027'
    """Indicates that the device is hidden within a combination."""

    DEVICE_NO_LOCATION_SET = '16019'
    """Indicates that the device has no location set."""

    DEVICE_SERIAL_NUMBER_INVALID = '16020'
    """Indicates that the device's serial number is invalid."""

    # Device authorization and modification codes
    DEVICE_NOT_AUTHORIZED = '16002'
    """Indicates that the device is not authorized for the operation."""

    DEVICE_TYPE_NOT_EXISTS = '16004'
    """Indicates that the specified device type does not exist."""

    DEVICE_TYPE_NOT_MODIFIABLE = '16005'
    """Indicates that the device type cannot be modified."""

    DEVICE_CANNOT_BE_DISABLED = '16010'
    """Indicates that this device cannot be disabled."""

    BOUND_TO_SCENARIOS = '16011'
    """Indicates that the device is bound to scenarios and cannot be altered."""

    UNASSIGNED_DEVICE_CANNOT_BE_COMBINED = '16012'
    """Indicates that an unassigned device cannot be part of a combination."""

    DEVICE_COMBINATION_EXISTS = '16013'
    """Indicates that a combination already exists for the device."""

    DEVICE_NOT_IN_GROUP = '16014'
    """Indicates that the device is not in any group."""

    # Command and protocol related codes
    COMMAND_ENCODING_NOT_DEFINED = '16008'
    """Indicates that command encoding is not defined."""

    SYSTEM_DEFAULT_COMMAND = '16009'
    """Indicates that the command is a system default command."""

    COMMAND_PROTOCOL_NOT_EXISTS = '16022'
    """Indicates that the command protocol does not exist."""

    COMMAND_PROTOCOL_NOT_AUTHORIZED = '16023'
    """Indicates that the command protocol is not authorized."""

    COMMAND_PROTOCOL_DATA_ERROR = '16024'
    """Indicates that there is an error in the command protocol data."""

    COMMAND_PROTOCOL_DUPLICATE = '16025'
    """Indicates that the command protocol is a duplicate."""

    COMMAND_PROTOCOL_LIMIT_EXCEEDED = '16026'
    """Indicates that the limit for command protocols has been exceeded."""

    # Combination and sensor limits
    COMBINATION_DATA_ERROR = '16006'
    """Indicates that there is an error with the combination data."""

    COMBINATION_LIMIT_EXCEEDED = '16007'
    """Indicates that the limit for combinations has been exceeded."""

    TEMPERATURE_SENSOR_LIMIT_EXCEEDED = '16028'
    """Indicates that the limit for temperature sensors has been exceeded."""

    HUMIDITY_SENSOR_LIMIT_EXCEEDED = '16029'
    """Indicates that the limit for humidity sensors has been exceeded."""

    VIRTUAL_DEVICE_LIMIT_EXCEEDED = '16030'
    """Indicates that the limit for virtual devices has been exceeded."""

    HOMEKIT_SUPPORT_LIMIT_EXCEEDED = '16031'
    """Indicates that the HomeKit support limit has been exceeded."""

    # Dashboard and lighting data errors
    DASHBOARD_CARD_ASSOCIATED_DATA_EXISTS = '16033'
    """Indicates that associated data exists for the dashboard card."""

    ALL_DAY_NATURAL_LIGHT_DATA_ERROR = '16035'
    """Indicates that there is an error with the all-day natural light data."""

    AFTERSALES_QR_INFO_NOT_EXISTS = '17001'
    """Indicates that the aftersales QR information does not exist."""

    AFTERSALES_QR_EXPIRED = '17002'
    """Indicates that the aftersales QR code has expired."""

    AFTERSALES_PENDING = '17003'
    """Indicates that the aftersales process is pending."""

    AFTERSALES_QR_SCANNED = '17004'
    """Indicates that the aftersales QR code has been scanned."""

    AFTERSALES_INFO_NOT_EXISTS = '17005'
    """Indicates that the aftersales information does not exist."""

    AFTERSALES_COMPLETED = '17006'
    """Indicates that the aftersales process has been completed."""

    AFTERSALES_INFO_EXPIRED = '17007'
    """Indicates that the aftersales information has expired."""

    FIRMWARE_UPGRADE_NOT_ALLOWED = '18001'
    """Indicates that the firmware upgrade is not allowed."""

    FIRMWARE_VERSION_ERROR = '18002'
    """Indicates that there is a firmware version error."""

    FIRMWARE_UPGRADE_IN_PROGRESS = '18003'
    """Indicates that a firmware upgrade is currently in progress."""

    FIRMWARE_VERSION_NOT_EXISTS = '18004'
    """Indicates that the specified firmware version does not exist."""

    TIMING_INFO_NOT_EXISTS = '19001'
    """Indicates that the timing information does not exist."""

    TIMING_INFO_NOT_AUTHORIZED = '19002'
    """Indicates that the timing information is not authorized."""

    TIMING_DATA_ERROR = '19003'
    """Indicates that there is an error with the timing data."""

    SCENE_INFO_NOT_EXISTS = '20001'
    """Indicates that the scene information does not exist."""

    SCENE_NOT_AUTHORIZED = '20002'
    """Indicates that the scene is not authorized for use."""

    SCENE_EXECUTION_FAILED = '20003'
    """Indicates that the scene execution has failed."""

    SCENE_DISABLED = '20004'
    """Indicates that the scene is disabled."""

    SCENE_CONFLICT_CONDITION = '20005'
    """Indicates that there are conflicting conditions for the scene."""

    TRIGGER_CONDITION_TIMING_CONFLICT = '20006'
    """Indicates a timing conflict with the trigger condition."""

    ADDITIONAL_CONDITION_TIMING_CONFLICT = '20007'
    """Indicates a timing conflict with an additional condition."""

    ADDITIONAL_CONDITION_GEOFENCE_CONFLICT = '20008'
    """Indicates a geofence conflict with an additional condition."""

    ADDITIONAL_CONDITION_GEOFENCE_DUPLICATE = '20009'
    """Indicates that there is a duplicate geofence condition."""

    ADDITIONAL_CONDITION_SENSOR_CONFLICT = '20010'
    """Indicates a sensor conflict with an additional condition."""

    ADDITIONAL_CONDITION_SENSOR_DUPLICATE = '20011'
    """Indicates that there is a duplicate sensor condition."""

    ADDITIONAL_CONDITION_DEVICE_DUPLICATE = '20012'
    """Indicates that there is a duplicate device condition."""

    ADDITIONAL_CONDITION_ENVIRONMENT_CONFLICT = '20013'
    """Indicates an environment conflict with an additional condition."""

    ADDITIONAL_CONDITION_ENVIRONMENT_DUPLICATE = '20014'
    """Indicates that there is a duplicate environment condition."""

    TRIGGER_ITEM_LIMIT = '20015'
    """Indicates that the limit for trigger items has been exceeded."""

    ADDITIONAL_ITEM_LIMIT = '20016'
    """Indicates that the limit for additional items has been exceeded."""

    EXECUTION_ITEM_LIMIT = '20017'
    """Indicates that the limit for execution items has been exceeded."""

    SCENE_NAME_DUPLICATE = '20018'
    """Indicates that the scene name is a duplicate."""

    SCENE_SYNC_IN_PROGRESS = '20019'
    """Indicates that scene synchronization is currently in progress."""

    SWITCH_PANEL_BINDING_EXISTS = '21001'
    """Indicates that a binding for the switch panel already exists."""

    DEVICE_TYPE_OVERLAP_NOT_ALLOWED = '21002'
    """Indicates that overlapping device types are not allowed."""

    MAX_LIMIT_EXCEEDED = '21003'
    """Indicates that the maximum limit has been exceeded."""

    DEVICE_ALREADY_MAPPED = '21004'
    """Indicates that the device is already mapped."""

    DISPLAY_TYPE_OVERLAP_NOT_ALLOWED = '21005'
    """Indicates that overlapping display types are not allowed."""

    BINDING_ONLY_LONG_PRESS = '21006'
    """Indicates that binding can only be done with a long press."""

    PANEL_LAYOUT_NOT_EXISTS = '21007'
    """Indicates that the panel layout does not exist."""

    BUTTON_ACTION_MISMATCH = '21008'
    """Indicates that there is a mismatch in button actions."""

    BINDING_ONLY_KNOB = '21009'
    """Indicates that binding can only be done using a knob."""

    MAPPED_NUMBER_EXISTS = '21010'
    """Indicates that the specified mapped number already exists."""

    MAPPING_COLLECTION_NOT_EXISTS = '21011'
    """Indicates that the mapping collection does not exist."""

    MAPPING_COLLECTION_FAILED = '21012'
    """Indicates that the mapping collection failed."""

    RELAY_GET_FAILED = '21013'
    """Indicates that getting the relay information failed."""

    DEVICE_MAX_MAPPED = '21014'
    """Indicates that the maximum number of devices has been mapped."""

    ENABLED_RELAY_EXISTS = '21015'
    """Indicates that an enabled relay already exists."""

    BUTTON_GET_FAILED = '21016'
    """Indicates that getting button information failed."""

    BUTTON_LIMIT_REACHED = '21017'
    """Indicates that the button limit has been reached."""

    BUTTON_ALREADY_ADDED = '21018'
    """Indicates that the button has already been added."""

    PANEL_MAPPING_RECORD_NOT_EXISTS = '21019'
    """Indicates that the panel mapping record does not exist."""

    PANEL_MAPPING_RECORD_NOT_AUTHORIZED = '21020'
    """Indicates that the panel mapping record is not authorized."""

    MEMBER_ASSIGN_DEVICE_PERMISSION = '22001'
    """Indicates that the member does not have permission to assign devices."""

    CANNOT_ADD_SELF = '22002'
    """Indicates that a member cannot add themselves."""

    INVITED_ALREADY = '22003'
    """Indicates that the member has already been invited."""

    INVITE_FAILED = '22004'
    """Indicates that the invite process has failed."""

    ACCOUNT_NOT_EXISTS = '22005'
    """Indicates that the specified account does not exist."""

    INVITE_INFO_NOT_EXISTS = '22006'
    """Indicates that the invite information does not exist."""

    INVITE_INFO_COMPLETED = '22007'
    """Indicates that the invite information has been completed."""


DEVICE_TYPE_MAP = {
    "1-001-001": "灯",
    "1-002-001": "风扇",
    "1-003-001": "开关",
    "1-004-001": "灯(不带电量)",
    "1-005-001": "风扇(不带电量)",
    "1-006-001": "开关(不带电量)",
    "1-006-002": "干接点信号继电器",
    "1-006-003": "门",
    "3-001-001": "调光",
    "3-001-002": "调光(DALI)",
    "3-002-001": "调色温",
    "3-002-002": "调色温(DALI)",
    "3-003-001": "调光调色温",
    "3-003-002": "调光调色温(DALI)",
    "3-004-001": "RGBW",
    "3-004-002": "RGBW(DALI)",
    "3-005-001": "RGB",
    "3-005-002": "RGB(DALI)",
    "3-006-001": "RGBCW (DALI)",
    "4-001-001": "杜亚开合帘",
    "4-001-002": "威仕达开合帘",
    "4-001-003": "奥特威开合帘",
    "4-001-004": "丰拓开合帘",
    "4-001-005": "创明开合帘",
    "4-001-006": "奥科开合帘",
    "4-002-001": "杜亚卷帘",
    "4-002-002": "威仕达卷帘",
    "4-002-003": "奥特威卷帘",
    "4-002-004": "奥科卷帘",
    "4-003-001": "杜亚百叶帘",
    "4-003-002": "奥特威百叶帘",
    "4-003-003": "乐屋百叶帘",
    "4-004-001": "博孚梦幻帘",
    "4-004-002": "乐屋梦幻帘",
    "4-004-003": "威仕达梦幻帘",
    "4-005-001": "达钶开窗器",
    "5-001-001": "通用空调",
    "5-001-002": "亿林中央空调",
    "5-001-003": "德姆瑞中央空调",
    "5-001-004": "慕驰空调",
    "5-001-005": "拉斐AC+二联供",
    "5-001-006": "海林空调",
    "5-001-007": "海林空调二联供",
    "5-001-008": "约克空调",
    "5-001-009": "弗雷克三合一环境面板",
    "5-001-010": "麦克维尔空调",
    "5-001-011": "富士通将军空调",
    "5-001-012": "零狗二联供温控器青春版",
    "5-001-013": "犀牛王二联供温控器",
    "5-001-014": "虚拟空调",
    "5-001-015": "迈斯线控网关",
    "5-001-016": "新晃空调温控",
    "5-001-017": "因立空调温控",
    "5-001-018": "迈斯集控网关",
    "5-001-019": "拓凡空调",
    "5-001-020": "海信精密空调",
    "5-001-021": "海尔中央空调",
    "5-001-022": "美的商用机型转接板（直流电机）",
    "5-001-023": "美的商用机型转接板（交流电机）",
    "5-001-024": "弗雷克三合一温控器",
    "5-001-025": "海林空调温控",
    "5-001-026": "视科温控",
    "5-001-027": "海信空调温控",
    "5-001-028": "曼瑞德温控",
    "5-001-029": "美的 V8modbus 网关(直流电机)",
    "5-001-030": "美的 V8modbus 网关（交流电机）",
    "5-001-031": "大金空调",
    "5-001-032": "东芝空调",
    "5-001-033": "中弘线控网关",
    "5-001-034": "中弘集控网关",
    "5-001-035": "广州洁控温控器",
    "5-001-036": "海信单元机",
    "5-002-001": "通用地暖",
    "5-002-002": "亿林地暖",
    "5-002-003": "慕驰地暖",
    "5-002-004": "海林地暖",
    "5-002-005": "弗雷克地暖",
    "5-002-006": "拉斐地暖温控器",
    "5-002-007": "亿林集中控制盒",
    "5-002-008": "虚拟地暖",
    "5-002-009": "拓凡温控地暖",
    "5-002-010": "因立温控地暖",
    "5-002-011": "拓凡地暖（TC）",
    "5-002-012": "曼瑞德地暖温控",
    "5-002-013": "弗雷克三合一温控器",
    "5-002-014": "视科温控",
    "5-002-015": "乐智地暖",
    "5-002-016": "伯克地暖温控",
    "5-002-017": "瑞好地暖温控",
    "5-003-001": "通用新风",
    "5-003-002": "博乐新风",
    "5-003-003": "净养新风",
    "5-003-004": "博乐新风EC",
    "5-003-005": "慕驰新风",
    "5-003-006": "松下新风",
    "5-003-007": "兰舍新风",
    "5-003-008": "曼瑞德新风",
    "5-003-009": "曼瑞德新风除湿机",
    "5-003-010": "艾科西尔新风",
    "5-003-011": "东芝新风",
    "5-003-012": "拉斐新风温控",
    "5-003-013": "迈迪龙新风主板",
    "5-003-014": "弗雷克新风",
    "5-003-015": "霍尼韦尔新风主板",
    "5-003-016": "日立全热交换器",
    "5-003-017": "松下双风速温控",
    "5-003-018": "百朗全热交换器",
    "5-003-019": "虚拟新风",
    "5-003-020": "托马仕新风",
    "5-003-021": "丹特卫顿新风",
    "5-003-022": "霍尼韦尔新风ERDH面板",
    "5-003-023": "士诺新风机",
    "5-003-024": "德业除湿机",
    "5-003-025": "三菱重工全热交换器",
    "5-003-026": "三菱重工海尔新风机",
    "5-003-027": "威特奇新风",
    "5-003-028": "东芝新风温控器",
    "5-003-029": "湿腾新风机",
    "5-003-030": "湿腾除湿机",
    "5-003-031": "威特奇新风（娜屋罗纳）",
    "5-003-032": "德普莱太新风转接板",
    "5-003-033": "爱迪士新风",
    "5-003-034": "欧井除湿新风",
    "5-003-035": "曼瑞德新风线控器",
    "5-003-036": "百朗新风线控器",
    "5-003-037": "威特奇娜屋罗",
    "5-003-038": "普瑞特除湿机",
    "5-003-039": "卡萨帝全热交换器",
    "5-003-040": "德姆瑞线控网关",
    "5-003-041": "霍德森新风线控器",
    "5-003-042": "布朗新风",
    "5-003-043": "麦克维尔单向流新风",
    "5-003-044": "布雷森新风控制器",
    "5-003-045": "科美臣新风",
    "5-003-046": "士诺新风",
    "5-003-047": "兰舍新风面板 L-3",
    "5-003-048": "威能新风控制器",
    "5-003-049": "大金全热交换器",
    "5-003-050": "东芝全热交换器",
    "5-003-051": "环都拓普新风控制器(HDK-19V)",
    "5-003-052": "环都拓普新风控制器(HDK-20A)",
    "5-003-053": "百朗新风线控器",
    "5-003-054": "沃森新风控制器",
    "5-003-055": "湿腾空气平衡器",
    "5-004-001": "开利热泵",
    "5-004-002": "艾默生热泵",
    "5-004-003": "特灵热泵(IOM)",
    "5-004-004": "特灵热泵(TG-A20/21M)",
    "5-004-005": "芬尼热泵",
    "5-004-006": "约克热泵",
    "5-004-007": "丹特卫顿热泵（X系列）",
    "5-004-008": "丹特卫顿热泵（客控中心）",
    "5-004-009": "开利热泵（开利ODU）",
    "5-004-010": "开利热泵（30RB065）",
    "5-005-001": "零狗青春版直流温控",
    "5-005-002": "零狗青春版三速温控",
    "5-005-003": "开利二联供",
    "5-005-004": "艾默生二联供",
    "5-005-005": "特灵二联供(IOM)",
    "5-005-006": "特灵二联供(TG-A20/21M)",
    "5-005-007": "特灵二联供(变频)",
    "5-005-008": "麦克维尔二联供",
    "5-005-009": "约克二联供",
    "5-005-010": "丹特卫顿二联供（温控通用）",
    "5-005-011": "丹特卫顿二联供（客控中心）",
    "5-005-012": "柯耐弗二联供",
    "5-005-013": "约克二联供温控",
    "5-005-014": "曼瑞德温控器",
    "5-005-015": "源牌控制柜",
    "5-005-016": "开利二联供系统",
    "5-005-017": "麦克维尔户式水机",
    "5-005-018": "约克天氟地水",
    "6-001-002": "按键面板(深度对接)",
    "6-002-003": "带按键的温控面板(深度对接)",
    "7-001-001": "温度",
    "7-002-001": "湿度",
    "7-003-001": "光照度",
    "7-004-001": "甲醛",
    "7-005-001": "PM2.5",
    "7-006-001": "二氧化碳",
    "7-007-001": "空气质量IAQ",
    "7-008-001": "人体感应",
    "7-008-002": "人体感应 T485",
    "7-008-003": "造作24G雷达呼吸存在感应",
    "7-009-001": "触发感应",
    "7-009-002": "光栅",
    "7-009-003": "造作红外人体感应",
    "7-009-004": "人体感应器",
    "7-009-005": "门磁",
    "7-009-006": "水浸传感器",
    "7-009-007": "烟雾报警器",
    "7-009-008": "可燃性气体报警器",
    "7-009-009": "泽泰存在感应",
    "7-009-010": "人体感应 （睿云联旋钮屏）",
    "7-010-001": "一氧化碳",
    "7-011-001": "TVOC",
    "7-012-001": "龙腾T-001-M33120-2-12",
    "7-012-002": "龙腾T-001-A1420-L-12",
    "7-013-001": "迈睿MSA043D 485",
    "7-014-001": "睿云联门口机",
    "7-014-002": "睿云联室内机",
    "7-015-001": "萤石摄像头",
    "7-015-002": "宇视视频摄像机",
    "8-001-001": "华尔思背景音乐",
    "8-001-002": "向往背景音乐S7/mini3S",
    "8-001-003": "向往背景音乐S8",
    "8-001-004": "声必可背景音乐",
    "8-001-005": "泊声背景音乐",
    "8-001-006": "Sonos背景音乐",
    "8-001-007": "悠达背景音乐",
    "107-001-001": "1P断路器",
    "107-001-002": "2P断路器",
    "107-001-003": "3P断路器",
    "107-001-004": "4P断路器",
    "107-002-001": "2P断路器",
    "107-002-002": "4P断路器",
    "107-003-001": "3P断路器",
}

GROUP_TYPE = {
    "Breaker": "断路器群组",
    "Light": "调光群组",
    "Color": "调色温群组",
    "LightColor": "双色温群组",
    "RGB": "RGB群组",
    "RGBW": "RGBW群组",
    "Retractable": "开合帘群组",
    "Roller": "卷帘群组",
    "Blind": "百叶帘群组",
    "VerticalBlind": "垂竖百叶帘群组"
}

HAVC_TYPE_MAP = {
    "5-001-001": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [15, 35],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet", "air"],
        "ac_lock_mode": ["lock", "half_lock", "unlock"],
        "ac_wind_speed": ["auto", "super_strong", "super_high", "high", "mid", "low", "super_low", "super_quiet"],
    },
    "5-001-002": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [10, 30],
        "ac_mode": ["cold", "hot"],
        "ac_lock_mode": ["lock", "unlock"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-003": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 32],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-004": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [15, 35],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-005": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 30],
        "ac_heat_set_temp_range": [16, 45],
        "ac_mix_set_temp_range": [16, 45],
        "ac_mode": ["cold", "hot", "fan", "wet", "heat", "mix"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-006": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [5, 35],
        "ac_mode": ["cold", "hot", "fan"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-007": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [5, 45],
        "ac_heat_set_temp_range": [16, 45],
        "ac_mix_set_temp_range": [16, 45],
        "ac_mode": ["cold", "hot", "fan", "heat", "mix"],
        "ac_lock_mode": ["lock", "unlock"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-008": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [5, 35],
        "ac_mode": ["cold", "hot", "fan", "heat", "mix"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-009": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [10, 32],
        "ac_mode": ["cold", "hot", "fan", "wet", "heat", "mix"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-010": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [5, 30],
        "ac_mode": ["cold", "hot", "fan", "wet", "auto", "heat", "mix", "wet_reheat"],
        "ac_wind_speed": ["auto", "super_high", "high", "mid_high", "mid", "mid_low", "low", "super_low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-011": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [10, 30],
        "ac_mode": ["cold", "hot", "fan", "wet", "auto"],
        "ac_wind_speed": ["auto", "high", "mid_high", "mid", "mid_low", "low", "super_low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-012": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [5, 35],
        "ac_mode": ["cold", "hot", "fan", "wet", "heat", "mix"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
        "ac_set_humidity": [40, 75],
    },
    "5-001-013": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [10, 35],
        "ac_mode": ["cold", "hot", "fan", "heat", "mix"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
        "ac_real_humidity_range": [0, 100],
    },
    "5-001-014": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [10, 35],
        "ac_mode": ["cold", "hot", "fan"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
        "ac_real_humidity_range": [0, 100],
    },
    "5-001-015": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 30],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-016": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [5, 45],
        "ac_mode": ["cold", "hot", "fan", "auto"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [0, 50],
    },
    "5-001-017": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [16, 32],
        "ac_mode": ["cold", "hot", "fan", "wet", "humidify"],
        "ac_wind_speed": ["high", "mid", "low"],
        "ac_real_temp_range": [0, 50],
        "ac_real_humidity_range": [0, 100],
    },
    "5-001-018": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [19, 30],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-019": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 30],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-20, 125],
        "ac_real_humidity_range": [0, 100],
    },
    "5-001-020": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 32],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
        "ac_real_humidity_range": [0, 100],
        "ac_set_humidity_range": [40, 80],
    },
    "5-001-021": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 30],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-20, 50],
    },
    "5-001-022": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [17, 30],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "super_high", "high", "mid_high", "mid", "mid_low", "low", "super_low"],
        "ac_real_temp_range": [-15, 80],
    },
    "5-001-023": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [17, 30],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-15, 80],
    },
    "5-001-024": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [10, 32],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
        "ac_real_humidity_range": [0, 100],
    },
    "5-001-025": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [10, 32],
        "ac_mode": ["cold", "hot", "fan"],
        "ac_wind_speed": ["auto", "super_high", "high", "mid", "low", "super_low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-026": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [17, 35],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["super_high", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-027": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 32],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-028": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [5, 45],
        "ac_mode": ["cold", "hot", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-029": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [17, 30],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "super_high", "high", "mid_high", "mid", "mid_low", "low", "super_low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-030": {
        "type": "ac",
        "ac_temp_step": 0.5,
        "ac_set_temp_range": [17, 30],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-031": {
        "type": "ac",
        "ac_temp_step": 0.1,
        "ac_set_temp_range": [16, 30],
        "ac_mode": ["auto", "cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "super_high", "high", "mid", "low", "super_low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-032": {
        "type": "ac",
        "ac_temp_step": 0.1,
        "ac_set_temp_range": [16, 30],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low", "super_low", "stop"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-033": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 30],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-034": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [16, 30],
        "ac_mode": ["cold", "hot", "fan", "wet"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-40, 60],
    },
    "5-001-035": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [18, 32],
        "ac_mode": ["cold", "hot"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [-20, 79],
    },
    "5-001-036": {
        "type": "ac",
        "ac_temp_step": 1,
        "ac_set_temp_range": [15, 30],
        "ac_mode": ["cold", "hot", "fan", "wet", "auto"],
        "ac_wind_speed": ["auto", "high", "mid", "low"],
        "ac_real_temp_range": [0, 45],
    },
    "5-002-001": {
        "type": "fh",
        "fh_temp_step": 0.1,
        "fh_lock_mode": ["lock", "half_lock", "unlock"],
        "fh_set_temp_range": [10, 30],
    },
    "5-002-002": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_lock_mode": ["lock", "half_lock", "unlock"],
        "fh_set_temp_range": [5, 35],
    },
    "5-002-003": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_lock_mode": ["lock", "half_lock", "unlock"],
        "fh_set_temp_range": [5, 35],
    },
    "5-002-004": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_lock_mode": ["lock", "unlock"],
        "fh_set_temp_range": [5, 35],
    },
    "5-002-005": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [10, 32],
        "fh_real_temp_range": [-20, 60],
    },
    "5-002-006": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [16, 45],
        "fh_real_temp_range": [-20, 60],
    },
    "5-002-007": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [16, 45],
        "fh_real_temp_range": [-20, 60],
    },
    "5-002-008": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [5, 35],
        "fh_real_temp_range": [-40, 60],
    },
    "5-002-009": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [16, 32],
        "fh_real_temp_range": [0, 50],
    },
    "5-002-010": {
        "type": "fh",
        "fh_temp_step": 0.5,
        "fh_set_temp_range": [16, 32],
        "fh_real_temp_range": [0, 50],
        "fh_real_humidity_range": [0, 100],
    },
    "5-002-011": {
        "type": "fh",
        "fh_temp_step": 0.5,
        "fh_set_temp_range": [16, 32],
        "fh_real_temp_range": [-20, 125],
        "fh_real_humidity_range": [0, 100],
    },
    "5-002-012": {
        "type": "fh",
        "fh_temp_step": 0.5,
        "fh_set_temp_range": [16, 32],
        "fh_lock_mode": ["lock", "unlock"],
        "fh_real_temp_range": [-20, 125],
    },
    "5-002-013": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [10, 32],
        "fh_real_temp_range": [-20, 60],
        "fh_real_humidity_range": [0, 100],
    },
    "5-002-014": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [17, 35],
        "fh_real_temp_range": [-20, 60],
    },
    "5-002-015": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [5, 35],
        "fh_real_temp_range": [-20, 60],
    },
    "5-002-016": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [5, 35],
        "fh_real_temp_range": [-20, 60],
    },
    "5-002-017": {
        "type": "fh",
        "fh_temp_step": 1,
        "fh_set_temp_range": [5, 35],
        "fh_lock_mode": ["lock", "unlock"],
        "fh_real_temp_range": [-20, 60],
    },

    "5-003-001": {
        "type": "fa",
        "fa_wind_speed": ["auto", "high", "mid", "low"],
        "fa_set_humidity_range": [20, 95],
        "fa_real_temp_range": [-40, 60],
    },
    "5-003-002": {
        "type": "fa",
        "fa_wind_speed": ["auto", "high", "mid", "low"],
        "fa_real_temp_range": [-40, 60],
        "fa_real_humidity_range": [0, 100],
        "fa_humidity_step": 1,
        "fa_set_humidity_range": [20, 95],
    },
    "5-003-003": {
        "type": "fa",
        "fa_wind_speed": ["auto", "high", "mid", "low"],
        "fa_real_temp_range": [-40, 60],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-004": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["auto", "manual", "timing"],
        "fa_real_temp_range": [0, 50],
        "fa_real_humidity_range": [1, 99],
    },
    "5-003-005": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
    },
    "5-003-006": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
        "fa_work_mode": ["heat_exchange", "common", "indoor_loop", "outdoor_loop"],
    },
    "5-003-007": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["manual", "timing"],
        "fa_real_temp_range": [-40, 60],
    },
    "5-003-008": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
    },
    "5-003-009": {
        "type": "fa",
        "fa_wind_speed": ["air", "clean", "wet"],
        "fa_work_mode": ["auto", "manual", "timing"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
        "fa_set_humidity_range": [0, 100],
    },
    "5-003-010": {
        "type": "fa",
        "fa_wind_speed": ["auto", "super_strong", "super_high", "high", "mid", "low", "super_low", "stop"],
        "fa_real_temp_range": [-20, 90],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-011": {
        "type": "fa",
        "fa_wind_speed": ["auto", "high", "mid", "low", "super_low", "stop"],
        "fa_work_mode": ["air", "wet"],
    },
    "5-003-012": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
    },
    "5-003-013": {
        "type": "fa",
        "fa_temp_step": 1,
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["indoor_loop", "fresh", "fresh_wet", "wet"],
        "fa_real_temp_range": [12, 99],
        "fa_real_humidity_range": [0, 100],
        "fa_set_humidity_range": [15, 35],
    },
    "5-003-014": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_set_humidity_range": [-20, 60],
        "fa_real_temp_range": [0, 100],
    },
    "5-003-015": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
    },
    "5-003-016": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
    },
    "5-003-017": {
        "type": "fa",
        "fa_wind_speed": ["high", "low"],
        "fa_real_temp_range": [0, 50],
    },
    "5-003-018": {
        "type": "fa",
        "fa_wind_speed": ["high", "low"],
        "fa_work_mode": ["fresh", "wet"],
        "fa_real_humidity_range": [0, 100],
        "fa_set_humidity_range": [0, 100],
    },
    "5-003-019": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_real_temp_range": [-40, 90],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-020": {
        "type": "fa",
        "fa_wind_speed": ["extreme_strong", "super_high", "high", "mid", "low", "super_low"],
        "fa_set_humidity_range": [40, 90],
        "fa_work_mode": ["auto", "manual", "program"],
        "fa_real_temp_range": [-20, 50],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-021": {
        "type": "fa",
        "fa_wind_speed": ["auto", "high", "low"],
        "fa_work_mode": ["wet", "ventilate"],
        "fa_real_temp_range": [-20, 50],
        "fa_real_humidity_range": [0, 100],
        "fa_humidity_step": 0.5,
        "fa_set_humidity_range": [30, 70],
    },
    "5-003-022": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
        "fa_work_mode": ["high", "mid", "low"],
        "fa_humidity_step": 1,
        "fa_set_humidity_range": [30, 70],
    },
    "5-003-023": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["auto", "manual"],
        "fa_real_temp_range": [-40, 125],
        "fa_real_humidity_range": [20, 95],
    },
    "5-003-024": {
        "type": "fa",
        "fa_wind_speed": ["high", "low"],
    },
    "5-003-025": {
        "type": "fa",
        "fa_wind_speed": ["high", "low"],
        "fa_work_mode": ["exhaust", "heat_exchange", "smart", "powerful"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-026": {
        "type": "fa",
        "fa_wind_speed": ["high", "low"],
        "fa_work_mode": ["exhaust", "heat_exchange", "smart", "powerful", "cold_room", "heat_room"],
    },
    "5-003-027": {
        "type": "fa",
        "fa_wind_speed": ["super_high", "high", "mid", "low"],
        "fa_work_mode": ["auto", "timing", "exhaust", "fresh", "energy_recycle", "night", "holiday"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-028": {
        "type": "fa",
        "fa_wind_speed": ["auto", "high", "mid", "low", "super_low", "stop"],
        "fa_work_mode": ["auto", "manual", "timing", "sleep"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-029": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["auto", "manual", "timing", "sleep"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-030": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["indoor_loop", "fresh", "fresh_wet", "wet"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
        "fa_humidity_step": 1,
        "fa_set_humidity_range": [10, 95],
    },
    "5-003-031": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
        "fa_work_mode": ["auto", "manual", "night", "holiday"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 99],
    },
    "5-003-032": {
        "type": "fa",
        "fa_wind_speed": ["high", "low"],
        "fa_work_mode": ["fresh", "wet"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
        "fa_humidity_step": 1,
        "fa_set_humidity_range": [0, 100],
    },
    "5-003-033": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "super_low", "stop"],
        "fa_work_mode": ["auto", "manual", "timing", "sleep"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-034": {
        "type": "fa",
        "fa_temp_step": 1,
        "fa_set_temp_range": [16, 30],
        "fa_work_mode": ["auto", "fresh", "clean", "wet"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
        "fa_humidity_step": 1,
        "fa_set_humidity_range": [0, 100],
    },
    "5-003-035": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
        "fa_real_temp_range": [-20, 60],
    },
    "5-003-036": {
        "type": "fa",
        "fa_wind_speed": ["super_high", "high", "mid", "low", "super_low", "stop"],
        "fa_work_mode": ["fresh", "clean", "cold_room", "sleep", "smart", "powerful"],
        "fa_real_temp_range": [-20, 60],
    },
    "5-003-037": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
        "fa_work_mode": ["night", "holiday"],
    },
    "5-003-038": {
        "type": "fa",
        "fa_temp_step": 1,
        "fa_set_temp_range": [16, 30],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [1, 100],
        "fa_humidity_step": 1,
        "fa_set_humidity_range": [0, 100],
    },
    "5-003-039": {
        "type": "fa",
        "fa_wind_speed": ["auto", "extreme_strong", "super_high", "high", "mid", "low", "super_low", "super_quiet"],
        "fa_work_mode": ["auto", "exhaust", "heat_exchange", "indoor_loop", "fresh", "pass"],
        "fa_real_temp_range": [-20, 60],
    },
    "5-003-040": {
        "type": "fa",
        "fa_wind_speed": ["extreme_strong", "super_high", "high", "mid", "low", "super_low", "super_quiet"],
    },
    "5-003-041": {
        "type": "fa",
        "fa_wind_speed": ["auto", "high", "mid", "low"],
        "fa_work_mode": ["auto", "manual", "timing"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 99],
    },
    "5-003-042": {
        "type": "fa",
        "fa_wind_speed": ["high", "low"],
    },
    "5-003-043": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
    },
    "5-003-044": {
        "type": "fa",
        "fa_temp_step": 1,
        "fa_set_temp_range": [16, 30],
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["auto", "manual", "timing"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 99],
    },
    "5-003-045": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["auto", "manual", "timing"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 100],
    },
    "5-003-046": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["auto", "manual", "timing"],
    },
    "5-003-047": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["manual", "timing"],
    },
    "5-003-048": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
        "fa_work_mode": ["auto", "manual", "sleep"],
    },
    "5-003-049": {
        "type": "fa",
        "fa_wind_speed": ["auto", "super_high", "high", "mid", "low", "super_low"],
        "fa_work_mode": ["auto", "heat_exchange", "common"],
    },
    "5-003-050": {
        "type": "fa",
        "fa_wind_speed": ["auto", "high", "mid", "low", "super_low", "stop"],
    },
    "5-003-051": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
        "fa_work_mode": ["auto", "manual"],
        "fa_real_temp_range": [0, 50],
    },
    "5-003-052": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low", "stop"],
        "fa_work_mode": ["auto", "manual"],
        "fa_real_temp_range": [0, 50],
    },
    "5-003-053": {
        "type": "fa",
        "fa_wind_speed": ["super_high", "high", "mid", "super_low", "low", "stop"],
        "fa_work_mode": ["fresh", "fresh_wet", "clean", "wet", "cold_room", "sleep", "smart", "powerful", "comfort",
                         "max", "frost",
                         "pipeline_clean"],
        "fa_real_temp_range": [-20, 60],
    },
    "5-003-054": {
        "type": "fa",
        "fa_wind_speed": ["high", "mid", "low"],
        "fa_work_mode": ["auto", "manual", "timing", "indoor_loop", "sleep", "pass"],
        "fa_real_temp_range": [-20, 60],
        "fa_real_humidity_range": [0, 99],
    },

    "5-004-001": {
        "type": "hp",
        "hp_temp_step": 0.5,
        "hp_set_temp_range": [5, 55],
        "hp_mode": ["cold", "hot"],
    },
    "5-004-002": {
        "type": "hp",
        "hp_temp_step": 0.5,
        "hp_set_temp_range": [7, 55],
        "hp_mode": ["cold", "hot"],
    },
    "5-004-003": {
        "type": "hp",
    },
    "5-004-004": {
        "type": "hp",
        "hp_temp_step": 1,
        "hp_set_temp_range": [5, 55],
        "hp_mode": ["cold", "hot"],
    },
    "5-004-005": {
        "type": "hp",
        "hp_temp_step": 0.5,
        "hp_set_temp_range": [35, 55],
        "hp_set_cold_temp_range": [7, 25],
        "hp_set_hot_temp_range": [25, 60],
        "hp_mode": ["cold", "hot", "hotwater", "cold_comp_hotwater", "hot_comp_hotwater"],
    },
    "5-004-006": {
        "type": "hp",
        "hp_temp_step": 1,
        "hp_set_temp_range": [5, 55],
        "hp_mode": ["cold", "hot", "cold_common_hotwater", "cold_fast_hotwater", "hot_common_hotwater",
                    "hot_fast_hotwater", "common_hotwater", "fast_hotwater", "water_pump_loop"],

    },
    "5-004-007": {
        "type": "hp",
        "hp_temp_step": 0.5,
        "hp_set_temp_range": [12, 50],
        "hp_mode": ["cold", "hot"],
    },
    "5-004-008": {
        "type": "hp",
        "hp_temp_step": 0.5,
        "hp_set_temp_range": [12, 55],
        "hp_mode": ["cold", "hot"],
    },
    "5-004-009": {
        "type": "hp",
        "hp_temp_step": 0.5,
        "hp_set_temp_range": [5, 55],
        "hp_mode": ["cold", "hot"],
    },
    "5-004-010": {
        "type": "hp",
        "hp_temp_step": 0.5,
        "hp_set_hot_temp_range": [30, 70],
        "hp_set_cold_temp_range": [-15, 30],
        "hp_mode": ["cold", "hot"],
    },
    "5-005-001": {
        "type": "tc",
        "tc_lock_mode": ["mode", "mode_wind", "mode_wind_temp", "unlock"],
        "tc_mode": ["cold", "hot", "wet", "ventilate", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid_high", "mid", "mid_low", "low", "super_low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [5, 35],
        "tc_set_humidity_range": [40, 75],
        "tc_real_temp_range": [-30, 97],
        "tc_humidity_step": 1,
        "tc_real_humidity_range": [0, 100],
    },
    "5-005-002": {
        "type": "tc",
        "tc_lock_mode": ["mode", "mode_wind", "mode_wind_temp", "unlock"],
        "tc_mode": ["cold", "hot", "wet", "ventilate", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [5, 35],
        "tc_set_humidity_range": [40, 75],
        "tc_real_temp_range": [-30, 97],
        "tc_humidity_step": 1,
        "tc_real_humidity_range": [0, 100],
    },
    "5-005-003": {
        "type": "tc",
        "tc_lock_mode": ["unlock", "lock"],
        "tc_mode": ["cold", "hot", "ventilate", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [5, 35],
        "tc_real_temp_range": [-20, 60],
    },
    "5-005-004": {
        "type": "tc",
        "tc_lock_mode": ["unlock", "lock"],
        "tc_mode": ["cold", "hot", "wet", "ventilate", "floorheat", "mix"],
        "tc_wind_speed": ["extreme_strong", "strong", "super_high", "high", "mid_high", "mid", "mid_low", "low",
                          "super_low", "extreme_low", "stop"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [5, 35],
        "tc_real_temp_range": [-30, 60],
    },
    "5-005-005": {
        "type": "tc",
        "tc_mode": ["cold", "hot", "wet", "ventilate", "floorheat", "smart_floorheat"],
        "tc_wind_speed": ["auto", "high", "mid_high", "mid", "mid_low", "low", "super_low", "stop"],
        "tc_temp_step": 1,
        "tc_set_temp_range": [5, 35],
        "tc_real_temp_range": [-20, 60],
    },
    "5-005-006": {
        "type": "tc",
        "tc_mode": ["auto", "cold", "hot", "wet", "ventilate", "floorheat", "smart_floorheat"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 1,
        "tc_set_temp_range": [15, 45],
        "tc_real_temp_range": [-30, 60],
    },
    "5-005-007": {
        "type": "tc",
        "tc_mode": ["auto", "cold", "hot", "wet", "ventilate", "floorheat", "smart_floorheat"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 1,
        "tc_set_temp_range": [0, 30],
        "tc_real_temp_range": [-20, 60],
    },
    "5-005-008": {
        "type": "tc",
        "tc_mode": ["auto", "cold", "hot", "wet", "ventilate", "wet_reheat", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "super_high", "high", "mid_high", "mid", "mid_low", "low", "super_low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [5, 30],
        "tc_real_temp_range": [-9.9, 70],
    },
    "5-005-009": {
        "type": "tc",
        "tc_mode": ["cold", "hot", "ventilate", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [5, 35],
        "tc_real_temp_range": [5, 35],
    },
    "5-005-010": {
        "type": "tc",
        "tc_mode": ["cold", "hot", "floorheat", "mix", "clean"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [10, 35],
        "tc_real_temp_range": [10, 35],
    },
    "5-005-011": {
        "type": "tc",
        "tc_mode": ["cold", "hot", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "super_high", "high", "mid", "low", "super_low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [10, 35],
        "tc_real_temp_range": [-20, 60],
    },
    "5-005-012": {
        "type": "tc",
        "tc_mode": ["cold", "hot", "ventilate", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 1,
        "tc_set_temp_range": [5, 35],
        "tc_real_temp_range": [-20, 60],
    },
    "5-005-013": {
        "type": "tc",
        "tc_mode": ["cold", "hot", "wet", "ventilate", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 1,
        "tc_set_temp_range": [5, 35],
        "tc_real_temp_range": [-20, 60],
        "tc_real_humidity_range": [0, 100]
    },
    "5-005-014": {
        "type": "tc",
        "tc_mode": ["cold", "hot", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [5, 35],
        "tc_real_temp_range": [-20, 60],
    },
    "5-005-015": {
        "type": "tc",
        "tc_temp_step": 1,
        "tc_set_temp_range": [5, 35],
        "tc_mode": ["cold", "hot", "ventilate"],
    },
    "5-005-016": {
        "type": "tc",
        "tc_mode": ["cold", "hot", "wet", "ventilate", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [15, 35],
        "tc_real_temp_range": [-20, 60],
    },
    "5-005-017": {
        "type": "tc",
        "tc_mode": ["auto", "cold", "hot", "wet", "ventilate", "wet_reheat", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "super_high", "high", "mid_high", "mid", "mid_low", "low", "super_low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [16, 30],
        "tc_real_temp_range": [-20, 60],
    },
    "5-005-018": {
        "type": "tc",
        "tc_mode": ["auto", "cold", "hot", "ventilate", "wet", "floorheat", "mix"],
        "tc_wind_speed": ["auto", "high", "mid", "low"],
        "tc_temp_step": 0.5,
        "tc_set_temp_range": [5, 35],
        "tc_real_temp_range": [-20, 60],
    }
}
