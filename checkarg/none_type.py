from checkarg.exceptions import ArgumentNoneError, NoneTypeErrorMessages


def is_not_none(value, argument_name: str = None, exception: Exception = None):
    if value is None:
        raise ArgumentNoneError(
            NoneTypeErrorMessages.not_none_message(argument_name), argument_name
        ) if exception is None else exception
