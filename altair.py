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
    DEFENT_BASE = 3
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
    def __init__(self, game):
        self.game = game
    def get_game(self):
        return game

    def get_evaluator(self):
        return game.evaluator

class Evaluator():
    def __init__(self):


class BaseGuardian:
    def __init__(self):


class GoldGuardian:
    def __init__(self):


class BorderGuardian:
    def __init__(self):
        self.borders = []

    def guard_individual(user_id):
        "stub"

    def guard_direction(direction):
        "stub"

if __name__ == '__main__':
