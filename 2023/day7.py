from collections import Counter
from functools import total_ordering
from operator import attrgetter

from utilities import input


cards = "23456789TJQKA"
joker_cards = "J23456789TQKA"


@total_ordering
class Hand:
    def __init__(self, cards: str, bid: int) -> None:
        self.cards_str: str = cards
        self.cards_counter: Counter = Counter(cards)
        self.bid: int = bid
        self.type = self.set_type()

    def __lt__(self, other) -> bool:
        if self.type != other.type:
            return self.type < other.type
        else:
            for a, b in zip(self.cards_str, other.cards_str):
                if cards.index(a) == cards.index(b):
                    continue
                else:
                    return cards.index(a) < cards.index(b)
            return False

    def __repr__(self) -> str:
        return f"<Hand - type {self.type}: {self.cards_str}, {self.bid}>"

    def set_type(self) -> None:
        counts = sorted(self.cards_counter.values(), reverse=True)
        if counts[0] == 5:
            return 7
        elif counts[0] == 4:
            return 6
        elif counts[0] == 3 and counts[1] == 2:
            return 5
        elif counts[0] == 3:
            return 4
        elif counts[0] == 2 and counts[1] == 2:
            return 3
        elif counts[0] == 2:
            return 2
        return 1


class Joker(Hand):
    def __init__(self, cards: str, bid: int) -> None:
        self.cards_str: str = cards
        self.other_cards = self.strip_jokers()
        self.cards_counter: Counter = Counter(self.other_cards)
        self.bid: int = bid
        self.jokers: int = cards.count("J")
        self.type = self.set_type()

    def __lt__(self, other) -> bool:
        if self.type != other.type:
            return self.type < other.type
        else:
            for a, b in zip(self.cards_str, other.cards_str):
                if joker_cards.index(a) == joker_cards.index(b):
                    continue
                else:
                    return joker_cards.index(a) < joker_cards.index(b)
            return False

    def set_type(self) -> None:
        counts = sorted(self.cards_counter.values(), reverse=True)
        if self.jokers == 5 or (counts[0] + self.jokers) == 5:
            return 7
        if counts[0] + self.jokers == 4:
            return 6
        if counts[0] + self.jokers == 3 and counts[1] == 2:
            return 5
        if counts[0] + self.jokers == 3:
            return 4
        if counts[0] == 2 and (self.jokers == 2 or counts[1] == 2):
            return 3
        if counts[0] == 2 or self.jokers:
            return 2
        return 1
    
    def strip_jokers(self) -> None:
        other_cards = ""
        for c in self.cards_str:
            if c != "J":
                other_cards += c
        return other_cards


def solve(hands: list[Hand]) -> int:
    hands.sort()

    winnings = 0
    for i, h in enumerate(hands, start=1):
        winnings += i * h.bid

    return winnings



if __name__ == "__main__":
    data = input.str_array_from_list("7.txt")
    hands = [Hand(line.split()[0], int(line.split()[1])) for line in data]
    joker_hands = [Joker(line.split()[0], int(line.split()[1])) for line in data]

    print(f"Part 1: {solve(hands)}")
    print(f"Part 2: {solve(joker_hands)}")
