import datetime

class RoomInfo:
    def __init__(self, room_no: str, room_name: str, house_no: str, floor_no: str,
                 create_time: str, seq: int, room_image: str):
        self.room_no = room_no
        self.room_name = room_name
        self.house_no = house_no
        self.floor_no = floor_no
        self.create_time = self._parse_datetime(create_time)
        self.seq = seq
        self.room_image = room_image

    @staticmethod
    def _parse_datetime(datetime_str: str) -> datetime.datetime:
        return datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
