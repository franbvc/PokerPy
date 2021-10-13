import random
from utils import card_numbers, card_suits

class CardDeck:
    def __init__(self):
        self.intial_deck = self.create_initial_deck()

  
    def create_initial_deck(self):
        deck = []
        for n in card_numbers:
            for suit in card_suits:
                deck.append((n, suit))

        random.shuffle(deck)
        return deck

    def deal_hole_cards(self):
        hole = []
        for i in range(2):
            hole.append(self.intial_deck.pop())
        
        return hole

    def deal_community_cards(self):
        c_cards = []
        for i in range(5):
            c_cards.append(self.intial_deck.pop())

        return c_cards

test = CardDeck()

print(test.intial_deck)
