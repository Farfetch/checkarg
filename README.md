![CheckArg](https://raw.githubusercontent.com/Farfetch/checkarg/master/docs/imgs/CheckArg_complete.png)

Guard clause library for Python projects, to validate arguments on every python function/method.


## Installation
You can install the latest version of this software from the Python package index (PyPI) as follows:

```bash
pip install --upgrade checkarg
```

## Usage

### Using CheckArg to validate numbers
In the following example we want to guarantee the first argument is a negative number and the second argument has a positive value or zero:
```python
import checkarg.number as Number

def doSomethingValid(negative_number: int, positive_number: int):
    Number.is_lower(negative_number, 0)
    Number.is_greater_or_equals(positive_number, 0)

    return negative_number, positive_number
```

### Using CheckArg to validate text
The following example requires the string of the first argument has some content, if it is None or empty or whith whitespaces, it will rise an exception. The second argument only requires to not be None or an empty message:
```python
import checkarg.text as Text

def doSomethingValid(title: str, body: str):
    Text.is_not_whitespace(title)
    Text.is_not_empty(body)

    return title, body
```

### Controlling the flow with the exceptions
Whenever the CheckArg detects something wrong it will raise different exceptions by the context. This is an example controling the flow execution:
```python
import checkarg.none_type as NoneType
import checkarg.number as Number
import checkarg.text as Text

from checkarg.exceptions import ArgumentNoneException, ArgumentException, ArgumentOutOfRangeException


def lookup_name(mapping, key: str, default: int):
    try:
        Number.is_greater(default, 0)
    except ArgumentOutOfRangeException:
        return None

    try:
        NoneType.is_not_none(mapping)
    except ArgumentNoneException:
        return default
    
    try:
        Text.is_not_empty(key)
    except (ArgumentException, ArgumentNoneException) as e:
        return default

    return mapping[key]
```


## Contributing
Read the [Contributing guidelines](CONTRIBUTING.md)


### Disclaimer
By sending us your contributions, you are agreeing that your contribution is made subject to the terms of our [Contributor Ownership Statement](https://github.com/Farfetch/.github/blob/master/COS.md)


## Maintainers
List of [Maintainers](MAINTAINERS.md)


## License
[MIT](LICENSE)
