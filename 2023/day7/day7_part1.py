import time
from typing import List

cardTypes = {'A': 12,
             'K': 11,
             'Q': 10,
             'J': 9,
             'T': 8,
             '9': 7,
             '8': 6,
             '7': 5,
             '6': 4,
             '5': 3,
             '4': 2,
             '3': 1,
             '2': 0}
handTypes = {
    6: "Five of a kind",
    5: "Four of a kind",
    4: "Full house",
    3: "Three of a kind",
    2: "Two pair",
    1: "One pair",
    0: "High card"
}

class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.strength = self.handStrength()
        self.bid = bid

    # These are used for sorted()
    def __lt__(self, other) -> bool:
        if self.strength == other.strength:
            for i in range(5): # assuming no incorrectly sized hands
                if cardTypes[self.cards[i]] == cardTypes[other.cards[i]]:
                    continue
                return cardTypes[self.cards[i]] < cardTypes[other.cards[i]]
        return self.strength < other.strength

    # The 'strength' of hand you have when playing camel
    def handStrength(self):
        """
        6: Five of a kind, where all five cards have the same label: AAAAA
        5: Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        4: Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        3: Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        2: Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        1: One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        0: High card, where all cards' labels are distinct: 23456
        """
        handCount = []
        for card in cardTypes:
            if card in self.cards:
                count = self.cards.count(card)
                # quick check if hand.count is 5, always return 6: Five of a kind
                if count == 5: return 6
                handCount.append(count)
        
        # Five of a kind has been accounted for in loop
        if 4 in handCount: return 5
        elif 3 in handCount and 2 in handCount: return 4
        elif 3 in handCount: return 3
        elif handCount.count(2) == 2: return 2
        elif 2 in handCount: return 1
        else: return 0

    def __repr__(self) -> str:
        return f"{self.cards}: {handTypes[self.strength]}"


def main():
    input_file = "day7_input.txt"

    with open(input_file) as f:
        lines = [ line.rstrip() for line in f.readlines() ]

        # hand: bid, strength
        hands = []

        for line in lines:
            cards, bid = line.split()
            hands.append(Hand(cards, int(bid)))


        # sort highest strenth to lowest
        sortedHands = sorted(hands)

        total = 0
        for rank, hand in enumerate(sortedHands):
            total += (rank + 1) * hand.bid
        print(total)



if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Time taken: {duration} seconds")