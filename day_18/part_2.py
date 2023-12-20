import sys
from itertools import islice


def up(coords):
    return (coords[0] - 1, coords[1])


def down(coords):
    return (coords[0] + 1, coords[1])


def right(coords):
    return (coords[0], coords[1] + 1)


def left(coords):
    return (coords[0], coords[1] - 1)


def sliding_window(iterable, n=2):
    args = [islice(iter(iterable), i, None) for i in range(n)]
    return zip(*args)


with open(sys.argv[1]) as file:
    data = file.read().splitlines()

commands = {
    '3': up,
    '1': down,
    '2': left,
    '0': right
}

current_node = (0, 0)
area = 0
total_visited_nodes = 0

for instruction in data:
    instruction = instruction.split(' ')[-1].strip('()#')

    command = instruction[-1]
    quantity = int(instruction[:-1], 16)

    for _ in range(quantity):
        old_node = current_node
        current_node = commands[command](current_node)

        area += old_node[0] * current_node[1]
        area -= old_node[1] * current_node[0]

        total_visited_nodes += 1

area = abs(area * 0.5)
internal_dots = area + 1 - total_visited_nodes / 2

total_area = int(total_visited_nodes + internal_dots)
print(total_area)
