import pytest

import checkarg.text as Text
from checkarg.exceptions import ArgumentError

valid_string_data = [
    pytest.param("data", id="Simple string"),
    pytest.param("data with whitespace ", id="String with an end whitespace"),
]

invalid_string_data = [
    pytest.param(None, id="None string"),
    pytest.param("", id="Empty string"),
    pytest.param("  ", id="Whitespace string"),
]

valid_string_or_list_data = [
    pytest.param("data", id="Simple string"),
    pytest.param(["data"], id="List with a string"),
]

invalid_string_or_list_data = [
    pytest.param("", id="Empty string"),
    pytest.param([], id="Empty list"),
]


@pytest.mark.parametrize("data", valid_string_data)
def test_is_not_whitespace__with_valid_data__does_nothing(data):
    # Arrange & Act & Assert
    Text.is_not_whitespace(data)


@pytest.mark.parametrize("data", invalid_string_data)
def test_is_not_whitespace__with_invalid_data__raises_argument_exception(data):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_not_whitespace(data)


@pytest.mark.parametrize("data", valid_string_or_list_data)
def test_is_not_empty__with_valid_data__does_nothing(data):
    # Arrange & Act & Assert
    Text.is_not_empty(data)


@pytest.mark.parametrize("data", invalid_string_or_list_data)
def test_is_not_empty__with_invalid_data__raises_argument_exception(data):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_not_empty(data)


@pytest.mark.parametrize("data", ["*", "*a", "_a"])
def test_is_alphanumeric__with_non_alphanumeric_data__raises_argument_exception(data):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_alphanumeric(data)


@pytest.mark.parametrize("data", ["a1", "A1"])
def test_is_alphanumeric__with_alphanumeric_data__does_nothing(data):
    # Arrange & Act & Assert
    Text.is_alphanumeric(data)


@pytest.mark.parametrize("data", ["a1", "A1", "a*"])
def test_is_alphabetic__with_non_alphabetic_data__raises_argument_exception(data):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_alphabetic(data)


def test_is_alphabetic__with_alphabetic_data__does_nothing():
    # Arrange & Act & Assert
    Text.is_alphabetic("data")


@pytest.mark.parametrize("data", ["a", "1.a"])
def test_is_number__with_non_number_data__raises_argument_exception(data):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_number(data)


@pytest.mark.parametrize("data", ["1", "1.0", "-1.0"])
def test_is_number__with_number_data__does_nothing(data):
    # Arrange & Act & Assert
    Text.is_number(data)


@pytest.mark.parametrize("data", ["a", "1.0"])
def test_is_integer__with_non_integer_data__raises_argument_exception(data):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_integer(data)


def test_is_integer__with_integer_data__does_nothing():
    # Arrange & Act & Assert
    Text.is_integer("1")


def test_is_lowercase__with_non_lowercase_data__raises_argument_exception():
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_lowercase("Data")


@pytest.mark.parametrize("data", ["a", "a_", "a1"])
def test_is_lowercase_with_lowercase_data__does_nothing(data):
    # Arrange & Act & Assert
    Text.is_lowercase(data)


def test_is_uppercase__with_non_uppercase_data__raises_argument_exception():
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_uppercase("Data")


@pytest.mark.parametrize("data", ["A", "A_", "A1"])
def test_is_uppercase_with_uppercase_data__does_nothing(data):
    # Arrange & Act & Assert
    Text.is_uppercase(data)


def test_has_length__with_different_length__raises_argument_exception():
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.has_length("data", 5)


def test_has_length_with_same_length__does_nothing():
    # Arrange & Act & Assert
    Text.has_length("data", 4)


def test_has_length_between__with_length_out_of_the_range__raises_argument_exception():
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.has_length_between("data", 1, 3)


def test_has_length_between__with_length_within_the_range__does_nothing():
    # Arrange & Act & Assert
    Text.has_length_between("data", 2, 6)


def test_is_equal_to__without_equal_data__raises_argument_exception():
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_equal_to("data", "data2")


def test_is_equal_to__with_equal_data__does_nothing():
    # Arrange & Act & Assert
    Text.is_equal_to("data", "data")


def test_is_not_equal_to__with_equal_data__raises_argument_exception():
    # Arrange & Act & Assert
    with pytest.raises(ArgumentError):
        Text.is_not_equal_to("data", "data")


def test_is_not_equal_to__without_equal_data__does_nothing():
    # Arrange & Act & Assert
    Text.is_not_equal_to("data", "data2")
