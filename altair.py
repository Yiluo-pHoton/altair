import colorfight
import datetime
import math
import copy


class Actions:
    DO_NOTHING = 0
    EVAL = 1
    SORT = 2


class CellStatus:
    MY_CELL = 0
    EMPTY = 1
    OCCUPIED_LOW = 2
    OCCUPIED_HIGH = 3


# Modes are for scanner to flag for the commander
class Modes:
    ATTACK = 0
    EXPANSION = 1
    DEFEND_BORDER = 2
    DEFEND_BASE = 3
    DEFEND_ENERGY = 4
    FILL = 5


# Directions are for commander to instruct evaluator where to evaluate
class Directions:
    NORTH = 0
    EAST = 1
    WEST = 2
    SOUTH = 3


class BaseStatus:
    SAFE_LOW =
    SAFE_HIGH =
    UNDER_ATTACK =
    TOUCHED_1 =
    TOUCHED_2 =
    TOUCHED_3 =
    TOUCHED_4 =


class Handler():
    '''
    Handler will allow access for other objects
    '''

    def __init__(self, altair):
        self.altair = altair

        def get_altair(self):
            return self.altair

    def get_game(self):
        return self.altair.g

    def get_evaluator(self):
        return self.altair.evaluator

    def get_base_guardians(self):
        return self.altair.base_guardians


class Evaluator:
    def __init__(self, handler):
        self.handler = handler


class BaseGuardian:
    '''
    BaseGuardian will flag statuses of each bases to the commander
    and act based on the commander's decision
    '''

    def __init__(self, handler):
        self.handler = handler


class GoldGuardian:
    '''
    GoldGuardian will flag statuses of each golden cell to the
    commander and act based on the commander's decision
    ''''

    def __init__(self, handler):
        self.handler = handler


class EnergyGuardian:
    '''
    EnergyGuardian will flag statuses of each golden cell to the
    commander and act based on the commander's decision
    It will also make sure there is enough energy for use
    '''
    def __init__(self, handler):
        self.handler =


class BorderGuardian:

    def __init__(self, handler):
        self.handler = handler
        self.borders = []

    def guard_individual(user_id):
        "stub"

    def guard_direction(direction):
        "stub"


class RankKeeper:

    def __init__(self, handler):
        self.handler = handler


class UserReporter:

    def __init__(self, handler):
        self.handler = handler


class Altair:
    '''
    Altair will be the commander that runs the game and am in charge of
    all of her factions
    '''
    def __init__(self):
        self.handler = (Handler(self))

        self.bases = []
        self.base_guardians = []


# Enter the main loop for the AI
if __name__ == '__main__':
