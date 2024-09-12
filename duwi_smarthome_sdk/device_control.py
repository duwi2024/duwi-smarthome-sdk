class Commands:
    def __init__(self, param_name, param_value):
        self.paramName = param_name
        self.paramValue = param_value

    def to_dict(self):
        return {'code': self.paramName, 'value': self.paramValue}


class ControlDevice:
    def __init__(self, device_no, house_no, is_group=False):
        self.device_no = device_no
        self.device_group_no = device_no
        self.house_no = house_no
        self.is_group = is_group
        self.commands = []

    def add_param_info(self, code, value):
        self.commands.append(Commands(code, value))

    def remove_param_info(self):
        self.commands.clear()

    def to_command_dict(self):
        return {cmd.paramName: cmd.paramValue for cmd in self.commands}

    def to_dict(self):
        commands_list = [cmd.to_dict() for cmd in self.commands]
        base_dict = {
            'houseNo': self.house_no,
            'commands': commands_list,
        }
        if self.is_group:
            base_dict['deviceGroupNo'] = self.device_group_no
        else:
            base_dict['deviceNo'] = self.device_no

        return base_dict
