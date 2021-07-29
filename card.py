
from enum import Enum

class Suit(Enum):
    SPADES = '♠️'
    CLUBS = '♣️'
    HEARTS = '♥️'
    DIAMONDS = '♦️'

    def __str__(self):
        return str(self.value)

class Face(Enum):
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'

    def __str__(self):
        return str(self.value)

class Card():

    def __init__(self, suit: Suit) -> None:
        self.suit = suit

class FaceCard(Card):

    def __str__(self) -> str:
        return str(self.face) + str(self.suit)

    def __init__(self, suit: Suit, face: Face) -> None:
        super().__init__(suit)
        self.face = face

class NumberCard(Card):

    def __str__(self) -> str:
        return str(self.number) + str(self.suit)

    def __init__(self, suit: Suit, number: int) -> None:
        super().__init__(suit)
        # Check that we have a valid integer for a numeric card
        assert number in range(2, 11)
        self.number = number

class Ace(Card):

    def __str__(self) -> str:
        return 'A' + str(self.suit)

    def __init__(self, suit: Suit) -> None:
        super().__init__(suit)