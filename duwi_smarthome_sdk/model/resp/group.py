from typing import Optional, Dict, Any
import datetime


class Group:
    def __init__(
            self,
            device_group_no: Optional[str] = None,
            device_group_name: Optional[str] = None,
            house_no: Optional[str] = None,
            room_no: Optional[str] = None,
            icon: Optional[str] = None,
            is_favorite: Optional[bool] = None,
            favorite_time: Optional[str] = None,
            create_time: Optional[str] = None,
            update_time: Optional[str] = None,
            execute_way: Optional[int] = None,
            device_group_type: Optional[str] = None,
            seq: Optional[int] = None,
            value: Optional[Dict[str, Any]] = None,
            sync_host_sequences: Optional[list] = None,
            device_no: Optional[str] = None,
            device_name: Optional[str] = None,
            terminal_sequence: Optional[str] = None,
            route_num: Optional[int] = None,
            device_type_no: Optional[str] = None,
            device_sub_type_no: Optional[str] = None,
            room_name: Optional[str] = None,
            floor_no: Optional[str] = None,
            floor_name: Optional[str] = None,
            is_use: Optional[bool] = None,
            is_online: Optional[bool] = None,
            create_time_device: Optional[str] = None,
            seq_device: Optional[int] = None,
            is_favorite_device: Optional[bool] = None,
            favorite_time_device: Optional[str] = None,
            key_binding_quantity: Optional[int] = None,
            key_mapping_quantity: Optional[int] = None,
            value_device: Optional[Dict[str, Any]] = None
    ):
        self.device_group_no = device_group_no
        self.device_group_name = device_group_name
        self.house_no = house_no
        self.room_no = room_no
        self.icon = icon
        self.is_favorite = is_favorite
        self.favorite_time = self.safe_parse_datetime(favorite_time)
        self.create_time = self.safe_parse_datetime(create_time)
        self.update_time = self.safe_parse_datetime(update_time)
        self.execute_way = execute_way
        self.device_group_type = device_group_type
        self.seq = seq
        self.value = value
        self.sync_host_sequences = sync_host_sequences
        # 设备属性
        self.device_no = device_no
        self.device_name = device_name
        self.terminal_sequence = terminal_sequence
        self.route_num = route_num
        self.device_type_no = device_type_no
        self.device_sub_type_no = device_sub_type_no
        self.room_name = room_name
        self.floor_no = floor_no
        self.floor_name = floor_name
        self.is_use = is_use
        self.is_online = is_online
        self.create_time_device = self.safe_parse_datetime(create_time_device)
        self.seq_device = seq_device
        self.is_favorite_device = is_favorite_device
        self.favorite_time_device = self.safe_parse_datetime(favorite_time_device)
        self.key_binding_quantity = key_binding_quantity
        self.key_mapping_quantity = key_mapping_quantity
        self.value_device = value_device

    @staticmethod
    def safe_parse_datetime(datetime_str: str) -> Optional[datetime.datetime]:
        if datetime_str == "" or datetime_str is None:
            return None
        return datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

    def __str__(self) -> str:
        return (f"Device Group No: {self.device_group_no}, "
                f"Device Group Name: {self.device_group_name}, "
                f"House No: {self.house_no}, "
                f"Room No: {self.room_no}, "
                f"Icon: {self.icon}, "
                f"Is Favorite: {self.is_favorite}, "
                f"Favorite Time: {self.favorite_time}, "
                f"Create Time: {self.create_time}, "
                f"Update Time: {self.update_time}, "
                f"Execute Way: {self.execute_way}, "
                f"Device Group Type: {self.device_group_type}, "
                f"Seq: {self.seq}, "
                f"Value: {self.value}, "
                f"Sync Host Sequences: {self.sync_host_sequences}, "
                # 设备属性
                f"Device No: {self.device_no}, "
                f"Device Name: {self.device_name}, "
                f"Terminal Sequence: {self.terminal_sequence}, "
                f"Route Num: {self.route_num}, "
                f"Device Type No: {self.device_type_no}, "
                f"Device Sub Type No: {self.device_sub_type_no}, "
                f"Room Name: {self.room_name}, "
                f"Floor No: {self.floor_no}, "
                f"Floor Name: {self.floor_name}, "
                f"Is Use: {self.is_use}, "
                f"Is Online: {self.is_online}, "
                f"Create Time (Device): {self.create_time_device}, "
                f"Seq (Device): {self.seq_device}, "
                f"Is Favorite (Device): {self.is_favorite_device}, "
                f"Favorite Time (Device): {self.favorite_time_device}, "
                f"Key Binding Quantity: {self.key_binding_quantity}, "
                f"Key Mapping Quantity: {self.key_mapping_quantity}, "
                f"Value (Device): {self.value_device}")
