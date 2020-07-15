from .utils import ArgumentNoneException


class NoneType:
    @staticmethod
    def is_not_none(value, argument_name: str = None, exception: Exception = None):
        if value is None:
            raise ArgumentNoneException(
                argument_name
            ) if exception is None else exception
