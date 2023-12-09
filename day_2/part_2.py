import re
from pprint import pp
from functools import reduce

def parse_round(round_line):
    round = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for color in round.keys():
        m = re.search(f'(\d+) {color}', round_line)

        if m is not None:
            round[color] = int(m.group(1))

    return round


def parse_rounds(game):
    return [parse_round(item.strip()) for item in game.split(';')]


def min_set(game_line):
    min_round = {}
    rounds = parse_rounds(game_line)

    min_round['red'] = max(round['red'] for round in rounds)
    min_round['green'] = max(round['green'] for round in rounds)
    min_round['blue'] = max(round['blue'] for round in rounds)

    return min_round



def min_set_power(line):
    pp(min_set(line))
    return reduce(lambda x, y: x * y, min_set(line).values())


total = 0

with open('input.txt') as f:
    for line in f:
        # pp(line)
        total += min_set_power(line)

    print(total)
