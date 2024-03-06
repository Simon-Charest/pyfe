from numpy import ndarray
from numpy.random import choice


def initialize_board(size: int, density=0.5) -> ndarray:
    """Initialize the board with random cells."""

    return choice([0, 1], size=(size, size), p=[1 - density, density])
