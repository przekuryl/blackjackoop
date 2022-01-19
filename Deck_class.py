from CardGame.Card_class import Card, suits, ranks
import random


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_deck(self):
        # there is 52 of cards, init brings them with non-random deck
        random.shuffle(self.all_cards)

    def take_one(self):
        return self.all_cards.pop()

    def add_one(self, card):
        return self.all_cards.append(card)