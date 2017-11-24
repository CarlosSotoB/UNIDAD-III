# Author: Jose Carlos Soto Barco
#description: a decorator in the function

from functools import wraps


def make_blink(function):
    """ Defines the decorator """

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to  the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


#Apply the decorator here!
@make_blink
def hello_word():
    """ Original function! """

    return "Hello, Word!"

# Check the result of decorating
print(hello_word())
# Check if the function name is till the name of function being decorated
print(hello_word.__name__)
# Check if the docstring is still the same as that of the function being decorated
print(hello_word.__doc__)
