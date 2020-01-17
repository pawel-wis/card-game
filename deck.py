import random
import cards


class Deck:
    def __init__(self):
        self.deck_cards = []
        
    def shuffle(self):
        random.shuffle(self.deck_cards)
    
    def fill(self):
        pass
    
    
    
class PokerDeck(Deck):
    
    def fill(self):
        # Filling deck with each color cards
        for i in range(len(cards.CARD_COLORS)):
            color = cards.CARD_COLORS[i]
            for i in range(len(cards.CARD_NAMES)):
               name = cards.CARD_NAMES[i]
               short_name = cards.CARD_SHORTNAMES[name]
               power = cards.CARD_POWER[short_name]
               card_color = color
               card = cards.Card(name, short_name, power, card_color)
               self.deck_cards.append(card)
                
                
    def shuffle(self):
        random.shuffle(self.deck_cards)
        
    
    def __str__(self):
        return f"Deck:\n{self.deck_cards}"