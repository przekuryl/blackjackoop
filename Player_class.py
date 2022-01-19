from BlackJack.Bank_class import Bank
from BlackJack.Hand_class import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = Bank(500)
        self.hand = Hand()

    def bet(self, value):
        pass
