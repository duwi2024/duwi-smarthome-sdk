class Control:
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return f"Code: {self.code}, Message: {self.message}"