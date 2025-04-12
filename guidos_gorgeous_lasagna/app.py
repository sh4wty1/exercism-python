"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2  # time per layer in minutes


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """Calculate the preparation time in minutes.

    :param layers: int - number of layers.
    :return: int - preparation time in minutes.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time (prep + bake).

    :param layers: int - number of layers.
    :param elapsed_bake_time: int - baking time elapsed.
    :return: int - total time in minutes.
    """
    return elapsed_bake_time + preparation_time_in_minutes(layers)
