"""
Implementation of the MasterMind game.
"""
import random

from mmapi.common.enums import KeyPegs, PegColors


class MasterMindBoard:
    """
    Representation of MasterMind decoding board and the actions that can be \
    executed by the codemaker and the codebreaker.
    """

    #: Codemaker's code length.
    CODE_LENGTH = 4

    def __init__(self, code=None):
        """
        Class initialization.

        :param code: Codemaker's code to be broken. Should consist of \
            four code pegs. If not value passed the code is randomly \
            generated.
        :type code: tuple
        """
        if code:
            self.code = code
        else:
            self.code = [random.choice(list(PegColors))
                         for x in range(self.CODE_LENGTH)]

        self.history = []

    def restart(self, code):
        """
        Restarts the game. Clean the history and sets a new codemaker's code.

        :param code: Codemaker's code to be broken.
        """
        self.code = code
        self.history = []

    def take_a_guess(self, code_guess):
        """
        Represents the action of the codebreaker when guessing. It returns \
        the corresponding feedback.

        :param code_guess: The codebreaker code pegs guess.
        :type code_guess: tuple
        :return: The feedback from the codemaker.
        :rtype: list
        """
        self.history.append(code_guess)
        second_pass_code = []
        second_pass_guess = []
        feedback = []

        # 1st pass to find black key pegs
        for i in range(self.CODE_LENGTH):
            if code_guess[i] == self.code[i]:
                feedback.append(KeyPegs.BLACK)
            else:
                second_pass_code.append(self.code[i])
                second_pass_guess.append(code_guess[i])

        # 2nd pass to find white key pegs
        color_matches = set(second_pass_code) & set(second_pass_guess)
        feedback.extend([KeyPegs.WHITE] * len(color_matches))

        return feedback
