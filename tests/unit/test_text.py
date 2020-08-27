import pytest

import checkarg.text as Text
from checkarg.exceptions import ArgumentException

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
    _ = Text.is_not_whitespace(data)


@pytest.mark.parametrize("data", invalid_string_data)
def test_is_not_whitespace__with_invalid_data__rises_argument_exception(data):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentException):
        _ = Text.is_not_whitespace(data)


@pytest.mark.parametrize("data", valid_string_or_list_data)
def test_is_not_empty__with_valid_data__does_nothing(data):
    # Arrange & Act & Assert
    _ = Text.is_not_empty(data)


@pytest.mark.parametrize("data", invalid_string_or_list_data)
def test_is_not_empty__with_invalid_data__rises_argument_exception(data):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentException):
        _ = Text.is_not_empty(data)
