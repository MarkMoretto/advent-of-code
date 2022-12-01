
"""
Purpose: Advent of Code challenge
Day: 22
Date created: 2020-12-22

Contributor(s):
    Mark M.
"""
import re
from utils import current_file, day_number, get_lines, read_data


# If testing, set DEBUG to True for a smaller data set.
DEBUG: bool = True


# Import data
if DEBUG:
    raw_data = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

else:
    # Current file filepath
    thisfile = current_file(__file__)

    # AOC day number
    DAY_NO: int = day_number(thisfile.stem)

    raw_data = read_data(f"day-{DAY_NO}-input.txt")

# raw_data = read_data(f"day-22-input.txt")

# Split data into lines for further processing.  Skip any missing or blank lines.
raw_data = raw_data.replace("\r", "")
raw_data = re.sub(r"Player \d:\n?", "", raw_data)

p1, p2 = raw_data.split("\n\n")
p1cards = list(map(int, p1.split("\n")))
p2cards = list(map(int, p2.split("\n")))

while True:
    p1card = p1cards.pop(0)
    p2card = p2cards.pop(0)
    if p1card > p2card:
        # print(f"Payer 1 wins hand: {p1card} -- {p2card}")
        p1cards.extend([p1card, p2card])
    else:
        # print(f"Payer 2 wins hand: {p1card} -- {p2card}")
        p2cards.extend([p2card, p1card])

    if len(p1cards) <= 0:
        winner = p2cards
        break
    elif len(p2cards) <= 0:
        winner = p1cards
        break

result = sum(map(lambda x, y: x*y, winner, list(range(len(winner), 0, -1))))
print(f"Part 1: The total point value is: {result}")



# Part 2
"""
Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of rounds with a few changes:

* Before either player deals a card, if there was a previous round in this game that
had exactly the same cards in the same order in the same players' decks, the game
instantly ends in a win for player 1. Previous rounds from other games are not
considered. (This prevents infinite games of Recursive Combat, which everyone agrees
is a bad idea.)
* Otherwise, this round's cards must be in a new configuration; the players begin the
round by each drawing the top card of their deck as normal.
* If both players have at least as many cards remaining in their deck as the value of
the card they just drew, the winner of the round is determined by playing a new game
of Recursive Combat (see below).
* Otherwise, at least one player must not have enough cards left in their deck to
recurse; the winner of the round is the player with the higher-value card.

"""





