from pprint import pp
from copy import copy


class Scratchcard:
    def __init__(self, card_id, numbers, winning_numbers):
        self.card_id = card_id
        self.numbers = numbers
        self.winning_numbers = winning_numbers

    def extra_cards(self):
        return len(self.winning_numbers & self.numbers)

    def __repr__(self):
        return f'Scratchcard(card_id={self.card_id}, numbers={self.numbers}, winning_numbers={self.winning_numbers})'


def parse_card(line):
    line = line.strip()

    card_id = int(line.split(':')[0].split(' ')[-1])
    winning_numbers = {int(i) for i in line.split(':')[1].split(' | ')[0].split(' ') if i.isdigit()}
    scratched_numbers = {int(i) for i in line.split(':')[1].split(' | ')[1].split(' ') if i.isdigit()}

    return Scratchcard(card_id, scratched_numbers, winning_numbers)


with open('input.txt') as f:
    total_points = 0

    scratchcards = [parse_card(line) for line in f]
    max_id = max(card.card_id for card in scratchcards)

    for scratchcard in scratchcards:
        first_duplicate_card = scratchcard.card_id + 1
        last_duplicate_card = first_duplicate_card + scratchcard.extra_cards()

        cards_to_update = []
        for i in range(first_duplicate_card, last_duplicate_card):
            c = next(card for card in scratchcards if card.card_id == i)

            if c is not None:
                cards_to_update.append(c)

        scratchcards.extend(cards_to_update)

    print(len(scratchcards))
