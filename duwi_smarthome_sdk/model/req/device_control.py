class Commands:
    def __init__(self, param_name, param_value):
        self.paramName = param_name
        self.paramValue = param_value

    def to_dict(self):
        return {
            'code': self.paramName,
            'value': self.paramValue
        }


class ControlDevice:
    def __init__(self, device_no, house_no):
        self.device_no = device_no
        self.house_no = house_no
        self.commands = []

    def add_param_info(self, code, value):
        commands = Commands(code, value)
        self.commands.append(commands)

    def remove_param_info(self):
        self.commands.clear()

    def to_dict(self):
        commands_list = [
            command.to_dict()
            for command in self.commands
        ]

        return {
            'deviceNo': self.device_no,
            'houseNo': self.house_no,
            'commands': commands_list,
        }
