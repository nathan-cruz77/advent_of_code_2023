import sys
from pprint import pp
from collections.abc import Iterable


STEPS = 65 + 131 * 3


def enumerate_n(iterable, start=0, n=1):
    count = start

    for item in iterable:
        if isinstance(item, Iterable) and n > 1:
            for index, value in enumerate_n(iter(item), start=start, n=n - 1):
                if not isinstance(index, Iterable):
                    index = [index]

                yield tuple([count, *index]), value
        else:
            yield count, item

        count += 1


def find_node(matrix, value):
    return next(coords for coords, item in enumerate_n(matrix, n=2) if item == value)


def node_neighbors(node, matrix):
    x, y = node

    neighbors = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

    return [n for n in neighbors if matrix[n[0] % len(matrix)][n[1] % len(matrix[0])] != '#']


with open(sys.argv[1]) as file:
    matrix = [list(line) for line in file.read().splitlines()]

start_node = find_node(matrix, 'S')

queue = [{start_node}]

steps = 0
while steps < STEPS:
    current_nodes = queue.pop()

    next_nodes = set()

    for current_node in current_nodes:
        for neighbor in node_neighbors(current_node, matrix):
            next_nodes.add(neighbor)

    queue.append(next_nodes)

    steps += 1

print(len(next_nodes))
