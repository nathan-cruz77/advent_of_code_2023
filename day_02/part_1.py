import re
from pprint import pp

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


def is_possible(line):
    for round in parse_rounds(line):
        if round['red'] > 12 or round['green'] > 13 or round['blue'] > 14:
            return False

    return True


total = 0

with open('input.txt') as f:
    for idx, line in enumerate(f):
        if is_possible(line):
            total += idx + 1

    print(total)
