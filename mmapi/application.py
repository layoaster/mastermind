"""
The base Flask application container/wrapper.
"""
from flask import Flask
from flask_cors import CORS

from mmgame.board import MasterMindBoard


class ApplicationContainer:
    """
    An application wrapper to configure/initialize the Flask app.
    """
    #: Flask app/module name.
    APP_NAME = 'mmapi'

    def __init__(self, game_board=None):
        self.app = None
        self.prepare_app()
        self.game_board = game_board if game_board is not None else self.get_game()

    def prepare_app(self):
        """
        Prepares the actual Flask application, and sets up the configuration \
        accordingly.
        """
        self.app = Flask(self.APP_NAME)
        self.app.config.from_object('mmapi.config.Config')
        CORS(self.app, origins=self.app.config['CORS_ACCEPTED_ORIGINS'])

        # Map urls with and without a trailing slash to the same endpoint.
        self.app.url_map.strict_slashes = False

    def get_game(self):
        """
        Instantiate the game board class.
        :return: The mastermind board object.
        :rtype: :class:`mmgame.board.MasterMindBoard`
        """
        return MasterMindBoard()

    def register_blueprints(self):
        """
        Does the blueprint registering part.
        """
        # Local import due to flask/blueprint circular imports.
        from mmapi.views import api_bp
        self.app.register_blueprint(api_bp, url_prefix='/api')


def get_app():
    """
    Returns an actual application instance.

    :returns: The application instance.
    :rtype: :class:`ApplicationContainer`
    """
    return ApplicationContainer()
