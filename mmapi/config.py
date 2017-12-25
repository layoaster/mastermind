"""
The application/Flask default configuration.
"""
from mmgame.configfetch import BooleanValue, Configuration, Value


class Config(Configuration):
    """
    The Flask/app default configuration.
    """
    #: The prefix to be used for environment variables for this class
    _prefix = 'MASTERMIND_FLASK_'

    #: Flask Debug flag
    DEBUG = BooleanValue(True)

    TESTING = BooleanValue(False)

    JSONIFY_PRETTYPRINT_REGULAR = BooleanValue(True)

    ENABLE_PROFILING = BooleanValue(False)

    CORS_ACCEPTED_ORIGINS = Value('*')
