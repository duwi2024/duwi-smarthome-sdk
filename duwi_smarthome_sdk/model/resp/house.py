from typing import Optional
import datetime


class HouseInfo:
    def __init__(
            self,
            house_no: str,
            house_name: str,
            house_image_url: Optional[str],
            address: str,
            location: str,
            seq: int,
            create_time: str,
            deliver_time: str,
            host_count: int,
            device_count: int,
            lan_secret_key: str
    ):
        self.house_no = house_no
        self.house_name = house_name
        self.house_image_url = house_image_url or None  # 可能为空字符串
        self.address = address
        self.location = location
        self.seq = seq
        self.create_time = self._parse_datetime(create_time)
        self.deliver_time = self._parse_datetime(deliver_time)
        self.host_count = host_count
        self.device_count = device_count
        self.lan_secret_key = lan_secret_key

    @staticmethod
    def _parse_datetime(datetime_str: str) -> datetime.datetime:
        return datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

    def __str__(self) -> str:
        return (f"House No: {self.house_no}, "
                f"House Name: {self.house_name}, "
                f"House Image URL: {self.house_image_url}, "
                f"Address: {self.address}, "
                f"Location: {self.location}, "
                f"Sequence: {self.seq}, "
                f"Create Time: {self.create_time}, "
                f"Deliver Time: {self.deliver_time}, "
                f"Host Count: {self.host_count}, "
                f"Device Count: {self.device_count}, "
                f"Lan Secret Key: {self.lan_secret_key}")
