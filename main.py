import deck



if __name__ == '__main__':
    my_deck = deck.PokerDeck()
    my_deck.fill()
    my_deck.shuffle()
    
    for card in my_deck.deck_cards:
        print(card)