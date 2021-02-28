from .error_messages import DefaultErrorMessages


class ArgumentError(ValueError):
    def __init__(self, message, argument_name):
        self.message = (
            message
            if message
            else DefaultErrorMessages.default_argument_message(argument_name)
        )


class ArgumentNoneError(ArgumentError):
    pass


class ArgumentOutOfRangeError(ArgumentError):
    pass
