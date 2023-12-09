from pprint import pp
from copy import copy


class Scratchcard:
    def __init__(self, card_id, numbers, winning_numbers):
        self.card_id = card_id
        self.numbers = numbers
        self.winning_numbers = winning_numbers

    def extra_cards(self):
        return len(self.winning_numbers & self.numbers)


def parse_card(line):
    line = line.strip()

    card_id = int(line.split(':')[0].split(' ')[1])
    winning_numbers = {int(i) for i in line.split(':')[1].split(' | ')[0].split(' ') if i.isdigit()}
    scratched_numbers = {int(i) for i in line.split(':')[1].split(' | ')[1].split(' ') if i.isdigit()}

    return Scratchcard(card_id, scratched_numbers, winning_numbers)


with open('test_input.txt') as f:
    total_points = 0

    scratchcards = [parse_card(line) for line in f]
    max_id = max(card.card_id for card in scratchcards)

    for scratchcard in scratchcards:
        scratchcards.extend({card for card in scratchcards if card.id in range(scratchcard + 1, scratchcard.extra_cards() + 1)})

    print(len(scratchcards))
