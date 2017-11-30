import colorfight


class BaseKeeper:
    my_bases = [] # (base, status)
    def __init__(self):
        'stub'


class EnergyKeeper:
    my_energy = []
    available_energy = []
    all_energy = []
    def __init__(self):
        'stub'


class GoldKeeper:
    my_gold = []
    available_gold = []
    all_gold = []
    def __init__(self):
        'stub'


class PlayerKeeper:
    player_num = 0
    rank = []
    def __init__(self):
        'stub'

    def get_ranking(self):
        'stub'


if __name__ == '__main__':
    my_cells = []
    my_border = []

    g.colorfight.Game()
    g.joinGame('Silvers')

    def defense_power(cell):
        return 'stub'

    def distance_c_2_c(cell, cell):
        return 'stub'

    def distance_c_2_l(cell, range):
        return 'stub'

    def distance_l_2_l(range, range):
        return 'stub'

    def attack_base(x, y):
        return 'stub'

    def attack_gold(x, y):
        return 'stub'

    def attack_energy(x, y):
        return 'stub'

    def defend_base(x, y):
        'stub'

    def defend_energy(x, y):
        'stub'

    def defend_gold(x, y):
        'stub'

    def report_user(user_id):
        return 'stub'

    def energy_appropriateness(action):
        return 'stub'

    def get_closest_resource():
        return 'stub'

    def get_border_range(direction):
        return 'stub'

    def get_terrain_range(direction):
        return 'stub'

    def get_least_dense_range():
        return 'stub'

    def eval_global_val(x, y):
        return 'stub'

    def get_global_max():
        return 'stub'

    def get_priority_task():
        return 'stub'

    def eval_local_val(x, y):
        return 'stub'

    def build_or_defend(base):
        return 'stub'
