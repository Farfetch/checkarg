from typing import List, TypeVar

import checkarg.none_type as NoneType
from checkarg.exceptions import ArgumentError, ListErrorMessages

T = TypeVar("T")


def is_not_empty(
    list: List, argument_name: str = None, exception: Exception = None
) -> None:
    """ Check if the given list is not empty """
    NoneType.is_not_none(list, argument_name, exception)
    if not list:
        raise ArgumentError(
            ListErrorMessages.is_not_empty_message(argument_name), argument_name
        ) if exception is None else exception


def has_length_lower(
    list: List,
    condition_value: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the given list length is lower than the condition_value """
    NoneType.is_not_none(list, argument_name, exception)
    if len(list) >= condition_value:
        raise ArgumentError(
            ListErrorMessages.has_length_lower_message(argument_name, condition_value),
            argument_name,
        ) if exception is None else exception


def has_length_greater(
    list: List,
    condition_value: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the given list length is greater than the condition_value """
    NoneType.is_not_none(list, argument_name, exception)
    if len(list) <= condition_value:
        raise ArgumentError(
            ListErrorMessages.has_length_greater_message(
                argument_name, condition_value
            ),
            argument_name,
        ) if exception is None else exception


def has_length_between(
    list: List,
    min_length: int,
    max_length: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the given list length is between min_length and max_length """

    has_length_greater(list, min_length - 1, argument_name, exception)
    has_length_lower(list, max_length + 1, argument_name, exception)


def is_length_equals(
    list: List,
    condition_value: int,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the given list length is equals than the condition_value """
    NoneType.is_not_none(list, argument_name, exception)
    if len(list) != condition_value:
        raise ArgumentError(
            ListErrorMessages.has_length_equals_message(argument_name, condition_value),
            argument_name,
        ) if exception is None else exception


def contains(
    list: List, element: T, argument_name: str = None, exception: Exception = None
) -> None:
    """ Check if a given element is present in the list """
    NoneType.is_not_none(list, argument_name, exception)
    if element not in list:
        raise ArgumentError(
            ListErrorMessages.contains_message(argument_name, element), argument_name
        ) if exception is None else exception


def has_all_elements_of_same_type(
    list: List, argument_name: str = None, exception: Exception = None
) -> None:
    """ Check if the elements' list are all of the same type """
    NoneType.is_not_none(list, argument_name, exception)

    if len(set(map(type, list))) != 1:
        raise ArgumentError(
            ListErrorMessages.all_elements_of_same_type_message(argument_name),
            argument_name,
        ) if exception is None else exception


def has_all_elements_of_type(
    list: List,
    expected_type: type,
    argument_name: str = None,
    exception: Exception = None,
) -> None:
    """ Check if the elements' list are all of a given type """
    NoneType.is_not_none(list, argument_name, exception)
    if any(type(element) != expected_type for element in list):
        raise ArgumentError(
            ListErrorMessages.all_elements_of_type_message(
                argument_name, expected_type
            ),
            argument_name,
        ) if exception is None else exception


def has_no_repeated_elements(
    list: List, argument_name: str = None, exception: Exception = None
) -> None:
    """ Check if the list has not repeated values """
    NoneType.is_not_none(list, argument_name, exception)
    if len(list) != len(set(list)):
        raise ArgumentError(
            ListErrorMessages.has_not_repeated_elements_message(argument_name),
            argument_name,
        ) if exception is None else exception
