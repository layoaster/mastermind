from flask import Blueprint, jsonify
from flask_restful import Api

from mmapi.common.exceptions import BaseGameException
from mmapi.resources.game import GameGuess, GameHistory, GameStart

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Game routes
api.add_resource(GameStart, '/game/start', endpoint='game_start')
api.add_resource(GameGuess, '/game/guess', endpoint='game_guess')
api.add_resource(GameHistory, '/game/history', endpoint='game_history')


# Custom app exceptions handler
@api_bp.errorhandler(Exception)
def handle_base_exceptions(e):
    """
    API custom exception handler.

    :param e: Exception raised in the application.
    :type e: :class:`onsearch.exceptions.BaseOnSearchException`
    :return: Details of the failure.
    :rtype: :class: `flask.wrappers.Response`
    """
    if isinstance(e, BaseGameException):
        response = jsonify(e.to_dict())
        response.status_code = e.status_code
        return response
    else:
        response = jsonify({'internalServerErrors': str(e)})
        response.status_code = 500
        return response
