"""
Serializers of the API views requests/responses.
"""
from marshmallow import fields, Schema, validate
from marshmallow_enum import EnumField

from mmgame import enums
from mmgame.board import MasterMindBoard


class GameStartSchema(Schema):
    """
    The game start request serializer.
    """
    #: Codemaker's code to set when starting a new game.
    codePattern = fields.List(
        EnumField(enums.PegColors, by_value=True),
        required=True,
        validate=validate.Length(min=MasterMindBoard.CODE_LENGTH)
    )


class GameGuessSchema(Schema):
    """
    The game guess request serializer.
    """
    #: Codebreaker's guess code.
    codeGuess = fields.List(
        EnumField(enums.PegColors, by_value=True),
        required=True,
        validate=validate.Length(min=MasterMindBoard.CODE_LENGTH)
    )


class GameGuessResponseSchema(Schema):
    """
    The game guess response serializer.
    """
    #: The feedback to return after a codebreaker's guess attempt.
    feedback = fields.List(
        EnumField(enums.KeyPegs, by_value=True),
        required=True,
        validate=validate.Length(max=MasterMindBoard.CODE_LENGTH)
    )


class GuessAttemptSchema(Schema):
    """
    A guess attempt nested schema serializer.
    """
    #: A single codebreaker's guess attempt.
    guess = fields.List(
        EnumField(enums.PegColors, by_value=True),
        required=True,
        validate=validate.Length(min=MasterMindBoard.CODE_LENGTH)
    )

    #: The correspondent guess feedback.
    feedback = fields.List(
        EnumField(enums.KeyPegs, by_value=True),
        required=True,
        validate=validate.Length(max=MasterMindBoard.CODE_LENGTH)
    )


class GameHistorySchema(Schema):
    """
    The game history response serializer.
    """
    #: The game history of attempts.
    history = fields.List(fields.Nested(GuessAttemptSchema), required=True)
