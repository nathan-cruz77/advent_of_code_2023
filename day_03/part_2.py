from pprint import pp
from collections.abc import Iterable
from itertools import product


class Gear:
    def __init__(self, pos):
        self.pos = pos

    def collide_with(self, part_number, schematic):
        return self.pos in part_number.neighbor_coords(schematic)

    def __repr__(self):
        return f'Gear(pos={self.pos})'


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

    def neighbor_coords(self, schematic):
        first_row = max(self.start[0] - 1, 0)
        last_row = min(self.end[0] + 1, len(schematic) - 1)

        first_col = max(self.start[1] - 1, 0)
        last_col = min(self.end[1] + 1, len(schematic[0]) - 1)

        return product(range(first_row, last_row + 1), range(first_col, last_col + 1))

    def is_valid(self, schematic):
        for x, y in self.neighbor_coords(schematic):
            if not schematic[x][y].isdigit() and schematic[x][y] != '.':
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


def parse_part_numbers(schematic):
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


def parse_gears(schematic):
    gears = []

    for pos, item in enumerate_n(schematic, n=2):
        if item == '*':
            gears.append(Gear(pos))

    return gears


with open('input.txt') as f:
    schematic = read_schematic(f)
    total = 0

    part_numbers = parse_part_numbers(schematic)
    gears = parse_gears(schematic)

    for gear in gears:
        colliding_part_numbers = [part_number for part_number in part_numbers if gear.collide_with(part_number, schematic)]

        if len(colliding_part_numbers) == 2:
            total += colliding_part_numbers[0].int_value * colliding_part_numbers[1].int_value

    print(total)
