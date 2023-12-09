from pprint import pp
from collections.abc import Iterable
from itertools import product


class PartNumber:
    def __init__(self, start, value):
        self.start = start
        self.end = None
        self.value = value

    def close(self):
        self.int_value = int(self.value)
        self.end = (self.start[0], self.start[1] + len(self.value) - 1)

    def append_value(self, value):
        self.value += value

    def is_valid(self, matrix):
        first_row = max(self.start[0] - 1, 0)
        last_row = min(self.end[0] + 1, len(matrix) - 1)

        first_col = max(self.start[1] - 1, 0)
        last_col = min(self.end[1] + 1, len(matrix[0]) - 1)

        coords = product(range(first_row, last_row + 1), range(first_col, last_col + 1))

        for x, y in coords:
            if not matrix[x][y].isdigit() and matrix[x][y] != '.':
                return True

        return False


    def __repr__(self):
        return f'PartNumber(start={self.start}, end={self.end}, value={self.value})'


def read_schematic(file):
    return [list(line)[:-1] for line in file]


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


def group_numbers(schematic):
    part_numbers = []

    current_part_number = None
    for (row, col), item in enumerate_n(schematic, n=2):
        if current_part_number is None and item.isdigit():
            current_part_number = PartNumber((row, col), item)
        elif current_part_number is not None and item.isdigit():
            current_part_number.append_value(item)
        elif current_part_number is not None and not item.isdigit():
            current_part_number.close()
            part_numbers.append(current_part_number)
            current_part_number = None

    return part_numbers


with open('input.txt') as f:
    schematic = read_schematic(f)
    total = 0

    for part_number in group_numbers(schematic):
        if part_number.is_valid(schematic):
            total += part_number.int_value

    print(total)
