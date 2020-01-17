class Player:
    def __init__(self):
        self.deck = None
        self.score = 0

    def add_score(self):
        self.score += 1

    def set_deck(self, deck):
        self.deck = deck
