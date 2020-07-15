from typing import List, Union

from .none_type import NoneType
from .utils import ArgumentException


class Text:
    @staticmethod
    def is_not_whitespace(
        value: str, argument_name: str = None, exception: Exception = None
    ):
        NoneType.is_not_none(value)
        if len(value.strip()) <= 0:
            raise ArgumentException(argument_name) if exception is None else exception

    @staticmethod
    def is_not_empty(
        value: Union[str, List], argument_name: str = None, exception: Exception = None
    ):
        NoneType.is_not_none(value)
        if isinstance(value, str):
            value = value.strip()
        if len(value) <= 0:
            raise ArgumentException(argument_name) if exception is None else exception
