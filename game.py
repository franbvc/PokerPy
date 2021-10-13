from cardDeck import CardDeck
from Player import Player

#later implement blind levels
# https://automaticpoker.com/poker-basics/poker-chip-values-for-home-game/
# https://www.cardschat.com/organize-home-game.php

class Game:
    def __init__(self, player_names, starting_chip_value, big_blind):
        self.deck = CardDeck()
        self.starting_chip_value = starting_chip_value
        self.big_blind = big_blind
        self.player_list = [Player(name, starting_chip_value) for name in player_names]


player_names = ['John', 'Steve', 'Daniel']
starting_chip_value = 3000
big_blind = 60
test = Game(player_names, starting_chip_value, big_blind)

print(test.player_list[1])