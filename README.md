![CheckArg](docs/imgs/CheckArg_complete.png)

Guard clause library for Python projects, to validate arguments on every python function/method.

## Usage

### Using CheckArg to validate numbers
In the following example we want to guarantee the first argument is a negative number and the second argument has a positive value or zero:
```python
from checkarg import Number

def doSomethingValid(negative_number: int, positive_number: int):
    Number.is_lower(negative_number, 0)
    Number.is_greater_or_equals(positive_number, 0)

    return negative_number, positive_number
```

### Using CheckArg to validate text
The following example requires the string of the first argument has some content, if it is None or empty or whith whitespaces, it will rise an exception. The second argument only requires to not be None or an empty message:
```python
from checkarg import Text

def doSomethingValid(title: str, body: str):
    Text.is_not_whitespace(title)
    Text.is_not_empty(body)

    return title, body
```

### Controlling the flow with the exceptions
Whenever the CheckArg detects something wrong it will raise different exceptions by the context. This is an example controling the flow execution:
```python
from checkarg import NoneType, Text, Number
from checkarg import ArgumentNoneException, ArgumentException, ArgumentOutOfRangeException


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

### Installation
Clone the repository with the following:

```bash
git clone https://github.com/Farfetch/checkarg.git
```

or add it to the project Pipfile:
```bash
checkarg = { editable = true, git = "git clone https://github.com/Farfetch/checkarg.git" }
```

## Contributing

Read the [Contributing guidelines](CONTRIBUTING.md)


## Maintainers

List of [Maintainers](MAINTAINERS.md)


## License

[MIT](LICENSE)


## Other Documentation
* [CHANGELOG.md](CHANGELOG.md)
* [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
* [DEPENDENCIES.md](DEPENDENCIES.md)
* [SECURITY.md](SECURITY.md)




