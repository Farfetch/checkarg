from typing import List, Union

import checkarg.none_type as NoneType
from checkarg.exceptions import ArgumentError, TextErrorMessages


def is_not_whitespace(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if len(value.strip()) <= 0:
        raise ArgumentError(
            TextErrorMessages.is_not_whitespace_message(argument_name), argument_name
        ) if exception is None else exception


def is_not_empty(
    value: Union[str, List], argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if isinstance(value, str):
        value = value.strip()
    if len(value) <= 0:
        raise ArgumentError(
            TextErrorMessages.is_not_empty_message(argument_name), argument_name
        ) if exception is None else exception


def is_alphanumeric(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if not value.isalnum():
        raise ArgumentError(
            TextErrorMessages.is_alphanumeric_message(argument_name, value),
            argument_name,
        ) if exception is None else exception


def is_alphabetic(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if not value.isalpha():
        raise ArgumentError(
            TextErrorMessages.is_alphabetic_message(argument_name, value), argument_name
        ) if exception is None else exception


def is_number(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    try:
        float(value)
    except Exception:
        raise ArgumentError(
            TextErrorMessages.is_number_message(argument_name, value), argument_name
        ) if exception is None else exception


def is_integer(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    try:
        int(value)
    except Exception:
        raise ArgumentError(
            TextErrorMessages.is_integer_message(argument_name, value), argument_name
        ) if exception is None else exception


def is_lowercase(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if not value.islower():
        raise ArgumentError(
            TextErrorMessages.is_lowercase_message(argument_name, value), argument_name
        ) if exception is None else exception


def is_uppercase(
    value: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if not value.isupper():
        raise ArgumentError(
            TextErrorMessages.is_uppercase_message(argument_name, value), argument_name
        ) if exception is None else exception


def has_length(
    value: str, length: int, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if len(value) != length:
        raise ArgumentError(
            TextErrorMessages.has_length_message(argument_name, len(value), length),
            argument_name,
        ) if exception is None else exception


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
        raise ArgumentError(
            TextErrorMessages.has_length_between_message(
                argument_name, len(value), min_lenght, max_lenght
            ),
            argument_name,
        ) if exception is None else exception


def is_equal_to(
    value: str, expected: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if value != expected:
        raise ArgumentError(
            TextErrorMessages.is_equal_to_message(argument_name, value, expected),
            argument_name,
        ) if exception is None else exception


def is_not_equal_to(
    value: str, expected: str, argument_name: str = None, exception: Exception = None
) -> None:
    NoneType.is_not_none(value, argument_name, exception)
    if value == expected:
        raise ArgumentError(
            TextErrorMessages.is_not_equal_to_message(argument_name, value),
            argument_name,
        ) if exception is None else exception
