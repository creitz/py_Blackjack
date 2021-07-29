
import random

from deck import Deck
from card import Card

class Pack():

    NUM_DECKS = 6

    def __init__(self) -> None:
        self.all_cards = self._generate_new_cards()

    def _generate_new_cards(self):

        # Create NUM_DECKS decks
        decks = [Deck() for _ in range(self.NUM_DECKS)]

        # Get all the cards from each deck, and shuffle them
        all_cards = [card for card in [deck.cards for deck in decks]]
        random.shuffle(all_cards)
        return all_cards

    def draw_card(self) -> Card:

        if len(self.all_cards) == 0:
            return None
        else:
            return self.all_cards.pop(0)
