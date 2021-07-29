
from card import Card, Suit, Face, FaceCard, NumberCard, Ace

class Deck():

    def __init__(self) -> None:
        all_cards = []
        for suit in Suit:
            # Create all the number and face cards for this suit
            number_cards = [NumberCard(suit=suit, number=i) for i in range(2, 11)]
            face_cards = [FaceCard(suit=suit, face=face) for face in Face]

            # Add the number, face, and ace cards to our list
            all_cards.extend(number_cards)
            all_cards.extend(face_cards)
            all_cards.append(Ace(suit=suit))

        # Save them
        self.cards = all_cards