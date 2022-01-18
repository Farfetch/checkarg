import pytest

import checkarg.list as List
from checkarg.exceptions import ArgumentError

single_int_element = [1]

seven_ints = [*range(0, 7)]
seven_strings = ["one", "two", "three", "four", "five", "six", "seven"]
seven_mix = [1, True, 3, "four", 5, False, 7.5]

no_repeated_ints = [*range(0, 3)]
no_repeated_string = ["one", "two", "three"]
no_repeated_mixed = [1, False, 3.5, "four"]

repeated_ints = [1, 2, 3, 2]
repeated_string = ["one", "two", "three", "two"]
repeated_mixed = [1, True, 3.5, True, "four", 3.5]

list_all_ints = [
    pytest.param(single_int_element, id="Single int"),
    pytest.param(seven_ints, id="Seven ints"),
    pytest.param(no_repeated_ints, id="No repeated ints"),
    pytest.param(repeated_ints, id="Repeated ints"),
]

list_all_strings = [
    pytest.param(seven_strings, id="Seven strings"),
    pytest.param(no_repeated_string, id="No repeated string"),
    pytest.param(repeated_string, id="Repeated string"),
]

not_repeated_lists = [
    pytest.param(no_repeated_ints, id="No repeated ints"),
    pytest.param(no_repeated_string, id="No repeated strings"),
    pytest.param(no_repeated_mixed, id="No repeated mix"),
]

repeated_lists = [
    pytest.param(repeated_ints, id="Repeated ints"),
    pytest.param(repeated_string, id="Repeated strings"),
    pytest.param(repeated_mixed, id="Repeated mix"),
]

empty_lists = [pytest.param([], id="Empty list"), pytest.param(None, id="None list")]

not_empty_lists = [
    pytest.param(single_int_element, id="List 1 int"),
    pytest.param(seven_ints, id="List 7 ints"),
    pytest.param(seven_strings, id="List 7 strings"),
    pytest.param(seven_mix, id="List 7 mix"),
]

lists_with_length_lower_than_3 = [
    pytest.param([], id="Empty list"),
    pytest.param(single_int_element, id="List 3 ints"),
    pytest.param(["one", "two"], id="List 2 items"),
    pytest.param([True, "three"], id="List 3 mix"),
]

lists_with_length_between_3_and_5 = [
    pytest.param([*range(0, 4)], id="List 4 ints"),
    pytest.param(["one", "two", "three", "four"], id="List 4 strings"),
    pytest.param([True, "three", 4.5], id="List 4 mix"),
]

lists_with_length_greater_than_5 = [
    pytest.param(seven_ints, id="List 7 ints"),
    pytest.param(seven_strings, id="List 7 strings"),
    pytest.param(seven_mix, id="List 7 mix"),
]

lists_with_length_equals_to_7 = [
    pytest.param(seven_ints, id="List 7 ints"),
    pytest.param(seven_strings, id="List 7 strings"),
    pytest.param(seven_mix, id="List 7 mix"),
]

lists_with_elements_same_type = [
    pytest.param(single_int_element, id="List 1 int"),
    pytest.param(seven_ints, id="List 7 ints"),
    pytest.param(seven_strings, id="List 7 strings"),
    pytest.param(
        [False, True, True, True, False, False, True, False], id="List 8 bool"
    ),
]

lists_with_elements_mixed_type = [
    pytest.param([1, 2.5, "three", 4, 5, 6, 7], id="List 7 mic"),
    pytest.param(["one", "two", "three", "four", 5, "six", "seven"], id="List 7 mixed"),
    pytest.param([1, True, 3, "four", 5, False, 7, 8.5], id="List 8 mix"),
]


@pytest.mark.parametrize("list", not_empty_lists)
def test_is_empty__with_items__does_nothing(list):
    # Arrange & Act & Assert
    List.is_not_empty(list)


@pytest.mark.parametrize("list", empty_lists)
def test_is_empty_with_no_elements_raise_exception(list):
    with pytest.raises(ArgumentError):
        List.is_not_empty(list)


@pytest.mark.parametrize("list", lists_with_length_lower_than_3)
def test_has_length_lower__with_length_lower_3__does_nothing(list):
    # Arrange & Act & Assert
    List.has_length_lower(list, 5)


@pytest.mark.parametrize("list", lists_with_length_greater_than_5)
def test_has_length_lower__with_length_greater_5__raise_exception(list):
    with pytest.raises(ArgumentError):
        List.has_length_lower(list, 5)


@pytest.mark.parametrize("list", lists_with_length_greater_than_5)
def test_has_length_greater__with_length_greater_5__does_nothing(list):
    # Arrange & Act & Assert
    List.has_length_greater(list, 5)


@pytest.mark.parametrize("list", lists_with_length_lower_than_3)
def test_has_length_greater__with_length_lower_3__raise_exception(list):
    with pytest.raises(ArgumentError):
        List.has_length_greater(list, 3)


@pytest.mark.parametrize("list", lists_with_length_between_3_and_5)
def test_has_length_between__with_length_between_3_5__does_nothing(list):
    # Arrange & Act & Assert
    List.has_length_between(list, 3, 5)


@pytest.mark.parametrize("list", lists_with_length_lower_than_3)
def test_has_length_between__with_length_lower_than_3__raise_exception(list):
    with pytest.raises(ArgumentError):
        List.has_length_between(list, 3, 5)


@pytest.mark.parametrize("list", lists_with_length_greater_than_5)
def test_has_length_between__with_length_greater_than_5__raise_exception(list):
    with pytest.raises(ArgumentError):
        List.has_length_between(list, 3, 5)


@pytest.mark.parametrize("list", lists_with_length_equals_to_7)
def test_is_length_equals__with_length_equal_7__does_nothing(list):
    # Arrange & Act & Assert
    List.is_length_equals(list, 7)


@pytest.mark.parametrize("list", lists_with_length_lower_than_3)
def test_is_length_equals__with_length_lower_than_3__raise_exception(list):
    with pytest.raises(ArgumentError):
        List.is_length_equals(list, 7)


@pytest.mark.parametrize(
    "list, element_in_list",
    [(no_repeated_ints, 2), (no_repeated_string, "one"), (no_repeated_mixed, 3.5)],
)
def test_contains__with_element_in_list__does_nothing(list, element_in_list):
    # Arrange & Act & Assert
    List.contains(list, element_in_list)


@pytest.mark.parametrize(
    "list, element_in_list",
    [(no_repeated_ints, 4), (no_repeated_string, "four"), (no_repeated_mixed, 2.8)],
)
def test_contains__with_element_not_in_list__raise_exception(list, element_in_list):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        List.contains(list, element_in_list)


@pytest.mark.parametrize("list", lists_with_elements_same_type)
def test_has_all_elements_of_same_type__with_same_types__does_nothing(list):
    # Arrange & Act & Assert
    List.has_all_elements_of_same_type(list)


@pytest.mark.parametrize("list", lists_with_elements_mixed_type)
def test_has_all_elements_of_same_type__with_mixed_types__raise_exception(list):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        List.has_all_elements_of_same_type(list)


@pytest.mark.parametrize("list", list_all_ints)
def test_has_all_elements_of_type__with_int_types__does_nothing(list):
    # Arrange & Act & Assert
    List.has_all_elements_of_type(list, int)


@pytest.mark.parametrize("list", list_all_strings)
def test_has_all_elements_of_type__with_string_types__does_nothing(list):
    # Arrange & Act & Assert
    List.has_all_elements_of_type(list, str)


@pytest.mark.parametrize("list", list_all_ints)
def test_has_all_elements_of_type__with_int_types__raise_exception(list):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        List.has_all_elements_of_type(list, str)


@pytest.mark.parametrize("list", list_all_strings)
def test_has_all_elements_of_type__with_string_types__raise_exception(list):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        List.has_all_elements_of_type(list, int)


@pytest.mark.parametrize("list", not_repeated_lists)
def test_has_no_repeated_elements__with_no_repeated_values__does_nothing(list):
    # Arrange & Act & Assert
    List.has_no_repeated_elements(list)


@pytest.mark.parametrize("list", repeated_lists)
def test_has_no_repeated_elements__with_repeated_values__raise_exception(list):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        List.has_no_repeated_elements(list)
