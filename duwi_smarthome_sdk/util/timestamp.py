import time


def current_timestamp() -> str:
    timestamp = int(time.time() * 1000)
    return str(timestamp)
