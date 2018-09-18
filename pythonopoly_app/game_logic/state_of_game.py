import random
from ..game_logic import dice

class Gamestate:
    players = []
    board_tiles = []

    def add_player(self, player):
        # check that no player has this name already
        players.append(player)

class Player:
    money = 1000
    name = ""
    current_position = 0

    def __init__(self, name):
        self.name = name
    #al = Player("Al")
