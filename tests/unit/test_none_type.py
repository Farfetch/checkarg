import pytest

import checkarg.none_type as NoneType
from checkarg.exceptions import ArgumentNoneError

valid_data = [
    pytest.param("", id="Empty string"),
    pytest.param(1, id="Number"),
    pytest.param([], id="Empty list"),
    pytest.param({}, id="Emtpy Dict"),
]


@pytest.mark.parametrize("data", valid_data)
def test_is_not_none__with_valid_data__does_nothing(data):
    # Arrange & Act & Assert
    NoneType.is_not_none(data)


def test_is_not_none__with_invalid_data__raises_argument_none_exception():
    # Arrange
    data = None
    # & Act & Assert
    with pytest.raises(ArgumentNoneError):
        NoneType.is_not_none(data)
