import random

CARD_NAMES = ('Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
CARD_SHORTNAMES = {'Nine': '9', 'Ten': '10', 'Jack': 'J', 'Queen': 'Q', 'King': 'K', 'Ace': 'A'}
CARD_POWER = {'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
CARD_COLORS = ('spades', 'hearts', 'diamonds', 'clubs')
CARD_COLORS_UNICODE = {'spades': '\u2660', 'hearts': '\u2661', 'diamonds': '\u2662', 'clubs': '\u2667'}

class Card:
    def __init__(self, name ,shortname, power, color):
        self.name = name
        self.shortname = shortname
        self.color = color
        
        
    def __str__(self):
        return f"{self.name} ({self.shortname}) of {self.color}"


def get_random():
    temp = random.randint(0, len(CARD_NAMES) - 1)
    name = CARD_NAMES[temp]
    short_name = CARD_SHORTNAMES[name]
    power = CARD_POWER[short_name]
    color = CARD_COLORS_UNICODE[CARD_COLORS[temp]]
    return Card(name, short_name, power, color)