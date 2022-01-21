from BlackJack.Bank_class import Bank
from BlackJack.Hand_class import Hand


class Player:
    def __init__(self, name, balance=500):
        self.name = name
        self.bank = Bank(balance)
        self.hand = Hand()

    def bet(self, value):
        pass
