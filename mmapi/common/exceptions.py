"""
Custom exception classes.
"""


class BaseGameException(Exception):
    """
    Base class for exceptions thrown in the application views.
    """
    status_code = 500
    message = 'Internal server error.'

    def __init__(self, message=None, status_code=None):
        Exception.__init__(self)
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code

    def to_dict(self):
        """
        Generate a dictionary of the errors adhering to the error schema.

        :return: Dictionary of errors adhering to the error schema.
        :rtype: dict
        """
        rv = {'genericErrors': [self.message]}
        return rv


class GameGuessInvalidException(BaseGameException):
    """
    Exception class, raise if the game is already over when guessing.
    """
    status_code = 403
    message = 'Game is over.'
