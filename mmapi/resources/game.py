"""
The MasterMind game API views.
"""
from flask import jsonify
from flask_restful import Resource

from mmapi import app_container
from mmapi.common import exceptions, serializers
from mmapi.common.utils import get_request_data, validation_error


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
        response = serializers.GameHistorySchema().dump(
            app_container.game_board.get_history()
        )
        if not response.errors:
            return jsonify(response.data)
        else:
            response = jsonify({'responseFieldErrors': response.errors})
            response.status_code = 400
            return response


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
        request_data = serializers.GameStartSchema().load(get_request_data())
        if request_data.errors:
            return validation_error(request_data.errors)

        code_pattern = tuple(request_data.data['codePattern'])
        app_container.game_board.restart(code=code_pattern)

        response = jsonify()
        return response


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
        # Checking the game is not over
        if app_container.game_board.over:
            raise exceptions.GameGuessInvalidException

        request_data = serializers.GameGuessSchema().load(get_request_data())
        if request_data.errors:
            return validation_error(request_data.errors)

        code_guess = tuple(request_data.data['codeGuess'])

        feedback = app_container.game_board.take_a_guess(code_guess)

        response = serializers.GameGuessResponseSchema().dump({'feedback': feedback})
        if not response.errors:
            return jsonify(response.data)
        else:
            response = jsonify({'responseFieldErrors': response.errors})
            response.status_code = 400
            return response
