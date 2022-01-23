from BlackJack.Card_class import Card
from BlackJack.Deck_class import Deck


class Hand:
    def __init__(self):
        self.cards_on = []
        self.value = 0
        self.ace_counter = 0

    def __str__(self):
        return f'Your hand contains: {len(self.cards_on)} cards with total value: {self.value}'

    def show_cards(self, amount_to_reveal='all'):
        if amount_to_reveal == 'all':
            for card in self.cards_on:
                print(card)
        elif amount_to_reveal == 'dealer':
            for card in self.cards_on[0:len(self.cards_on) - 1]:
                print(card)

    def add_card_from_deck(self, deck, amount=1):
        for num in range(0, amount):
            self.cards_on.append(deck.take_one())
        return self.cards_on

    def remove_all_cards(self):
        self.cards_on = []
        return self.cards_on

    def count_value_of_cards(self):
        self.value = 0
        self.ace_counter = 0
        for card in self.cards_on:
            if card.rank == 'Ace':
                self.ace_counter += 1
                self.value += 0
            else:
                self.value += card.value

        if self.ace_counter == 0:
            return self.value
        else:
            new_hand_values_below_21 = []
            for card in self.cards_on:
                if card.rank == 'Ace':
                    new_hand_values = list(map(lambda x: x + self.value, [1, 11]))
                    for new_hand_value in new_hand_values:
                        if new_hand_value > 21:
                            continue
                        else:
                            new_hand_values_below_21.append(new_hand_value)

            # if any value is more than 21 than just add ace as 1, and return value
            if len(new_hand_values_below_21) == 0:
                self.value += 1
                return self.value
            else:
                self.value = new_hand_values_below_21[
                    min(range(len(new_hand_values_below_21)), key=lambda i: abs(new_hand_values_below_21[i] - 21))]
                return self.value
