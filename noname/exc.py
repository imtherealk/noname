class ExitError(Exception):
    def __init__(self, code=0, message=None):
        self.code = code
        super().__init__(message)