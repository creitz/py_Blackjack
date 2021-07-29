
from decimal import Decimal

class Player():

    def __init__(self, player_number: int, start_dollars: Decimal):
        """
        Create a player with the given starting amount of money,
        """
        self.player_number = player_number
        self.dollars_remaining = start_dollars