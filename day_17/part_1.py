import sys
from heapq import heappush, heappop


def is_inside(coords, matrix):
    row, col = coords

    row_range = range(len(matrix))
    col_range = range(len(matrix[0]))

    return row in row_range and col in col_range


def a_star(matrix):
    starting_block = (0, 0)
    target_block = (len(matrix) - 1, len(matrix[0]) - 1)

    queue = [(0, starting_block, (0, 0), 0)]
    visited_blocks = set()

    total_heat_loss = 0

    while queue:
        heat_loss, current_block, direction, steps = heappop(queue)

        if not is_inside(current_block, matrix):
            continue

        if current_block == target_block:
            total_heat_loss = heat_loss
            break

        if (current_block, direction, steps) in visited_blocks:
            continue

        visited_blocks.add((current_block, direction, steps))

        if direction != (0, 0) and steps < 3:
            next_block = (current_block[0] + direction[0], current_block[1] + direction[1])

            if is_inside(next_block, matrix):
                heappush(queue, (
                    heat_loss + matrix[next_block[0]][next_block[1]],
                    next_block,
                    direction,
                    steps + 1
                ))

        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if d not in [(-direction[0], -direction[1]), direction]:
                next_block = (current_block[0] + d[0], current_block[1] + d[1])

                if is_inside(next_block, matrix):
                    heappush(queue, (
                        heat_loss + matrix[next_block[0]][next_block[1]],
                        next_block,
                        d,
                        1
                    ))


    return total_heat_loss


with open(sys.argv[1]) as file:
    matrix = []

    for line in file.read().splitlines():
        l = [int(item) for item in line]
        matrix.append(l)

print(a_star(matrix))
