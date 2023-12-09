import re
from pprint import pp

def positions(s):
    string_positions = {
        ('zero', 0): [],
        ('one', 1): [],
        ('two', 2): [],
        ('three', 3): [],
        ('four', 4): [],
        ('five', 5): [],
        ('six', 6): [],
        ('seven', 7): [],
        ('eight', 8): [],
        ('nine', 9): [],
        ('0', 0): [],
        ('1', 1): [],
        ('2', 2): [],
        ('3', 3): [],
        ('4', 4): [],
        ('5', 5): [],
        ('6', 6): [],
        ('7', 7): [],
        ('8', 8): [],
        ('9', 9): []
    }

    for k in string_positions.keys():
        string_positions[k] = [m.start() for m in re.finditer(k[0], s)]

    return string_positions


def get_line_calibration_value(line):
    items = [item for item in positions(line).items() if item[1] != []]

    first = sorted(items, key=lambda x: min(x[1]))[0][0][1]
    last = sorted(items, key=lambda x: max(x[1]), reverse=True)[0][0][1]

    print(f'{line.strip()} -> {first}{last}')

    return int(f'{first}{last}')


total = 0

with open('input.txt') as f:
    for line in f:
        total += get_line_calibration_value(line)

    print(total)
