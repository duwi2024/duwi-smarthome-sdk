from typing import Dict, Optional, Any
import datetime


class Device:
    def __init__(
            self,
            device_no: str,
            device_name: str,
            terminal_sequence: str,
            route_num: int,
            device_type_no: str,
            device_sub_type_no: str,
            house_no: str,
            room_no: str,
            room_name: str,
            floor_no: str,
            floor_name: str,
            is_use: bool,
            is_online: bool,
            create_time: str,
            seq: int,
            is_favorite: bool,
            favorite_time: str,
            key_binding_quantity: int,
            key_mapping_quantity: int,
            value: Dict[str, Any]
    ):
        self.device_no: str = device_no
        self.device_name: str = device_name
        self.terminal_sequence: str = terminal_sequence
        self.route_num: int = route_num
        self.device_type_no: str = device_type_no
        self.device_sub_type_no: str = device_sub_type_no
        self.house_no: str = house_no
        self.room_no: str = room_no
        self.room_name: str = room_name
        self.floor_no: str = floor_no
        self.floor_name: str = floor_name
        self.is_use: bool = bool(is_use)
        self.is_online: bool = is_online
        self.create_time: datetime.datetime = self.safe_parse_datetime(create_time)
        self.seq: int = seq
        self.is_favorite: bool = bool(is_favorite)
        self.favorite_time: datetime.datetime = self.safe_parse_datetime(favorite_time)
        self.key_binding_quantity: int = key_binding_quantity
        self.key_mapping_quantity: int = key_mapping_quantity
        self.value: Dict[str, Optional[bool, int, str]] = value

    @staticmethod
    def safe_parse_datetime(datetime_str: str) -> datetime.datetime | None:
        if datetime_str == "" or datetime_str is None:
            return None
        return datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

    def __str__(self) -> str:
        return (f"Device No: {self.device_no}, "
                f"Device Name: {self.device_name}, "
                f"Terminal Sequence: {self.terminal_sequence}, "
                f"Route Num: {self.route_num}, "
                f"Type No: {self.device_type_no}, "
                f"Sub Type No: {self.device_sub_type_no}, "
                f"House No: {self.house_no}, "
                f"Room No: {self.room_no}, "
                f"Is Use: {self.is_use}, "
                f"Is Online: {self.is_online}, "
                f"Create Time: {self.create_time}, "
                f"Seq: {self.seq}, "
                f"Is Favorite: {self.is_favorite}, "
                f"Favorite Time: {self.favorite_time}, "
                f"Key Binding Quantity: {self.key_binding_quantity}, "
                f"Key Mapping Quantity: {self.key_mapping_quantity}, "
                f"Value: {self.value}")
