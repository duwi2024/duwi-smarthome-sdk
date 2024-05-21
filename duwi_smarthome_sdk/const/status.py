from enum import Enum

class Code(Enum):
    # 成功
    SUCCESS = '10000'
    # 系统错误
    SYS_ERROR = '10001'
    # 账号或密码错误
    LOGIN_ERROR = '11000'
    # appKey异常
    APP_KEY_ERROR = '99001'
    # 签名错误
    SIGN_ERROR = '99002'
    # 时间戳请求超时
    TIMESTAMP_TIMEOUT = '99003'
    # 系统频率限制
    SYSTEM_RATE_LIMIT = '99004'
    # 系统分钟频率限制
    SYSTEM_MINUTE_RATE_LIMIT = '99005'
    # 系统小时频率限制
    SYSTEM_HOUR_RATE_LIMIT = '99006'
    # 网关系统错误
    GATEWAY_SYS_ERROR = '99999'


