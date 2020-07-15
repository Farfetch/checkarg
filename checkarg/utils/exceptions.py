class ArgumentException(Exception):
    def __init__(self, argument_name=None):
        if argument_name is not None:
            self.message = f"Argument name: {argument_name}"


class ArgumentNoneException(ArgumentException):
    pass


class ArgumentOutOfRangeException(ArgumentException):
    pass
