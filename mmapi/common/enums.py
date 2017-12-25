"""
Enumerated types used across the api/application.
"""
from enum import Enum


class PegColors(Enum):
    """
    The colors available for code pegs.
    """
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    YELLOW = 'yellow'
    PURPLE = 'purple'


class KeyPegs(Enum):
    """
    The representation of the key pegs. Black peg: correct color and order. \
    White peg: correct color but wrong position.
    """
    BLACK = 'black'
    WHITE = 'white'
