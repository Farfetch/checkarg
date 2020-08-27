from typing import Union

from checkarg.exceptions import ArgumentOutOfRangeException


def is_greater(
    value: Union[int, float],
    condition_value: Union[int, float],
    argument_name: str = None,
    exception: Exception = None,
):
    if value < condition_value:
        raise ArgumentOutOfRangeException(
            argument_name
        ) if exception is None else exception


def is_lower(
    value: Union[int, float],
    condition_value: Union[int, float],
    argument_name: str = None,
    exception: Exception = None,
):
    if value > condition_value:
        raise ArgumentOutOfRangeException(
            argument_name
        ) if exception is None else exception


def is_greater_or_equals(
    value: Union[int, float],
    condition_value: Union[int, float],
    argument_name: str = None,
    exception: Exception = None,
):
    if value < condition_value:
        raise ArgumentOutOfRangeException(
            argument_name
        ) if exception is None else exception


def is_lower_or_equals(
    value: Union[int, float],
    condition_value: Union[int, float],
    argument_name: str = None,
    exception: Exception = None,
):
    if value > condition_value:
        raise ArgumentOutOfRangeException(
            argument_name
        ) if exception is None else exception
