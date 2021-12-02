class DefaultErrorMessages:
    @staticmethod
    def default_argument_message(argument_name):
        return f"Argument name: {argument_name}"


class NoneTypeErrorMessages:
    @staticmethod
    def not_none_message(argument_name):
        return f"Argument {argument_name} shouldn't be None"


class NumberErrorMessages:
    @staticmethod
    def is_greater_message(argument_name, value, condition_value):
        return f"Argument {argument_name} with value {value} should be greater than {condition_value}"

    @staticmethod
    def is_lower_message(argument_name, value, condition_value):
        return f"Argument {argument_name} with value {value} should be lower than {condition_value}"

    @staticmethod
    def is_greater_or_equals_message(argument_name, value, condition_value):
        return f"Argument {argument_name} with value {value} should be greater than or equal to {condition_value}"

    @staticmethod
    def is_lower_or_equals_message(argument_name, value, condition_value):
        return f"Argument {argument_name} with value {value} should be lower than or equal to {condition_value}"


class TextErrorMessages:
    @staticmethod
    def is_not_whitespace_message(argument_name):
        return f"Argument {argument_name} shouldn't be only whitespaces"

    @staticmethod
    def is_not_empty_message(argument_name):
        return f"Argument {argument_name} shouldn't be empty"

    @staticmethod
    def is_alphanumeric_message(argument_name, value):
        return f"Argument {argument_name} should be alphanumeric instead of {value}"

    @staticmethod
    def is_alphabetic_message(argument_name, value):
        return f"Argument {argument_name} should be alphabetic instead of {value}"

    @staticmethod
    def is_number_message(argument_name, value):
        return f"Argument {argument_name} should be a number instead of {value}"

    @staticmethod
    def is_integer_message(argument_name, value):
        return f"Argument {argument_name} should be an integer instead of {value}"

    @staticmethod
    def is_lowercase_message(argument_name, value):
        return f"Argument {argument_name} should be lowercase instead of {value}"

    @staticmethod
    def is_uppercase_message(argument_name, value):
        return f"Argument {argument_name} should be uppercase instead of {value}"

    @staticmethod
    def has_length_message(argument_name, lenght_value, conditional_lenght):
        return f"Argument {argument_name} should have lenght of {conditional_lenght} instead of {lenght_value}"

    @staticmethod
    def has_length_between_message(
        argument_name, lenght_value, min_conditional_lenght, max_conditional_lenght
    ):
        return f"""
            Argument {argument_name} should have lenght between
            {min_conditional_lenght} and {max_conditional_lenght}
            instead of {lenght_value}"""

    @staticmethod
    def is_equal_to_message(argument_name, value, conditional_value):
        return f"Argument {argument_name} with value {value} should be equal to {conditional_value}"

    @staticmethod
    def is_not_equal_to_message(argument_name, value):
        return f"Argument {argument_name} shouldn't be equal to {value}"


class ListErrorMessages:
    @staticmethod
    def is_not_empty_message(argument_name):
        return f"Argument {argument_name} shouldn't be empty"

    @staticmethod
    def has_length_lower_message(argument_name, condition_value):
        return f"The length of argument {argument_name} should be lower than {condition_value}"

    @staticmethod
    def has_length_greater_message(argument_name, condition_value):
        return f"The length of argument {argument_name} should be higher than {condition_value}"

    @staticmethod
    def has_length_equals_message(argument_name, condition_value):
        return f"The length of argument {argument_name} should be equals to {condition_value}"

    @staticmethod
    def contains_message(argument_name, element):
        return f"The element {element} is not present in the argument {argument_name}"

    @staticmethod
    def all_elements_of_same_type_message(argument_name):
        return f"All the elements of the argument {argument_name} should be of the same type"

    @staticmethod
    def all_elements_of_type_message(argument_name, type):
        return f"All the elements of the argument {argument_name} should be of the type {type}"

    @staticmethod
    def has_not_repeated_elements_message(argument_name):
        return f"Argument {argument_name} shouldn't have repeated values"
