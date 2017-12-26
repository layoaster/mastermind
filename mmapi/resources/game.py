"""
The MasterMind game API views.
"""
from flask_restful import Resource

from mmapi import app_container


class GameHistory(Resource):
    """
    Provides an API to get the game history.
    """
    def get(self):
        """
        Returns game history.
        /game/history

        :return: Json response.
        :rtype: :class:`flask.wrappers.Response`
        """
        pass


class GameStart(Resource):
    """
    Provides an API to start a new game.
    """
    def post(self):
        """
        Starts a new game.
        /game/start

        :return: Json response.
        :rtype: :class:`flask.wrappers.Response`
        """
        pass


class GameGuess(Resource):
    """
    Provides an API to make a code guess.
    """
    def put(self):
        """
        Make a code guess and returns its feedback.
        /game/guess

        :return: Json response.
        :rtype: :class:`flask.wrappers.Response`
        """
        pass
