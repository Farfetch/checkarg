from typing import List, Union

import checkarg.none_type as NoneType
from checkarg.exceptions import ArgumentException


def is_not_whitespace(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if len(value.strip()) <= 0:
        raise ArgumentException(argument_name) if exception is None else exception


def is_not_empty(
    value: Union[str, List], argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if isinstance(value, str):
        value = value.strip()
    if len(value) <= 0:
        raise ArgumentException(argument_name) if exception is None else exception


def is_alphanumeric(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if not value.isalnum():
        raise ArgumentException(argument_name) if exception is None else exception


def is_alphabetic(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if not value.isalpha():
        raise ArgumentException(argument_name) if exception is None else exception


def is_number(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    try:
        float(value)
    except Exception:
        raise ArgumentException(argument_name) if exception is None else exception


def is_integer(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    try:
        int(value)
    except Exception:
        raise ArgumentException(argument_name) if exception is None else exception


def is_lowercase(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if not value.islower():
        raise ArgumentException(argument_name) if exception is None else exception


def is_uppercase(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if not value.isupper():
        raise ArgumentException(argument_name) if exception is None else exception


def has_length(
    value: str, length: int, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if len(value) != length:
        raise ArgumentException(argument_name) if exception is None else exception


def has_length_between(
    value: str,
    min_lenght: int,
    max_lenght: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    value_length = len(value)
    if value_length < min_lenght or value_length > max_lenght:
        raise ArgumentException(argument_name) if exception is None else exception


def is_equal_to(
    value: str, expected: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if value != expected:
        raise ArgumentException(argument_name) if exception is None else exception


def is_not_equal_to(
    value: str, expected: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if value == expected:
        raise ArgumentException(argument_name) if exception is None else exception
