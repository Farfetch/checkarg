import pytest

from checkarg import ArgumentOutOfRangeException, Number

positive_numbers = [
    pytest.param(1, id="Number one"),
    pytest.param(10, id="Number ten"),
    pytest.param(11, id="Number eleven"),
    pytest.param(11.0, id="Float number"),
]

negative_numbers = [
    pytest.param(-1, id="Negative one"),
    pytest.param(-10, id="Negative ten"),
    pytest.param(-11, id="Negative eleven"),
    pytest.param(-11.0, id="Float Negative number"),
]


@pytest.mark.parametrize("negative_number", negative_numbers)
def test_is_lower__with_lower_number__does_nothing(negative_number):
    # Arrange & Act & Assert
    _ = Number.is_lower(negative_number, 0)


@pytest.mark.parametrize("positive_number", positive_numbers)
def test_is_lower__with_greater_number__rises_argument_out_of_range_exception(
    positive_number
):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentOutOfRangeException):
        _ = Number.is_lower(positive_number, 0)


@pytest.mark.parametrize("negative_number", negative_numbers)
def test_is_lower_or_equals__with_lower_number__does_nothing(negative_number):
    # Arrange & Act & Assert
    _ = Number.is_lower_or_equals(negative_number, -1)


@pytest.mark.parametrize("positive_number", positive_numbers)
def test_is_lower_or_equals__with_greater_number__rises_argument_out_of_range_exception(
    positive_number
):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentOutOfRangeException):
        _ = Number.is_lower_or_equals(positive_number, 0)


@pytest.mark.parametrize("positive_number", positive_numbers)
def test_is_greater__with_greater_number__does_nothing(positive_number):
    # Arrange & Act & Assert
    _ = Number.is_greater(positive_number, 0)


@pytest.mark.parametrize("negative_number", negative_numbers)
def test_is_greater__with_greater_number__rises_argument_out_of_range_exception(
    negative_number
):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentOutOfRangeException):
        _ = Number.is_greater(negative_number, 0)


@pytest.mark.parametrize("positive_number", positive_numbers)
def test_is_greater_or_equals__with_lower_number__does_nothing(positive_number):
    # Arrange & Act & Assert
    _ = Number.is_greater_or_equals(positive_number, 1)


@pytest.mark.parametrize("negative_number", negative_numbers)
def test_is_greater_or_equals__with_greater_number__rises_argument_out_of_range_exception(
    negative_number
):
    # Arrange & Act & Assert
    with pytest.raises(ArgumentOutOfRangeException):
        _ = Number.is_greater_or_equals(negative_number, 0)
