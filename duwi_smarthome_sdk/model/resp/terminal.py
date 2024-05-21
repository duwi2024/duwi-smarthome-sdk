import datetime


class TerminalInfo:
    def __init__(self,
                 terminal_name: str,
                 terminal_sequence: str,
                 short_code: str,
                 product_model: str,
                 product_logo: str,
                 seq: int,
                 is_gateway: int,
                 host_sequence: str,
                 create_time: str,
                 product_show_model: str,
                 is_follow_online: bool,
                 is_online: bool):
        self.terminal_name = terminal_name
        self.terminal_sequence = terminal_sequence
        self.short_code = short_code
        self.product_model = product_model
        self.product_logo = product_logo
        self.seq = seq
        self.is_gateway = is_gateway
        self.host_sequence = host_sequence
        self.create_time = create_time
        self.product_show_model = product_show_model
        self.is_follow_online = is_follow_online
        self.is_online = is_online

    @staticmethod
    def _parse_datetime(datetime_str: str) -> datetime.datetime:
        return datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
