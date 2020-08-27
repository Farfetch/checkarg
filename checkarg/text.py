from typing import List, Union

import checkarg.none_type as NoneType
from checkarg.exceptions import ArgumentException


def is_not_whitespace(
    value: str, argument_name: str = None, exception: Exception = None
):
    NoneType.is_not_none(value)
    if len(value.strip()) <= 0:
        raise ArgumentException(argument_name) if exception is None else exception


def is_not_empty(
    value: Union[str, List], argument_name: str = None, exception: Exception = None
):
    NoneType.is_not_none(value)
    if isinstance(value, str):
        value = value.strip()
    if len(value) <= 0:
        raise ArgumentException(argument_name) if exception is None else exception
