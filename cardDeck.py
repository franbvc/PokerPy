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

test = CardDeck()

print(test.intial_deck)