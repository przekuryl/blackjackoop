class Bank:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return self.balance

    def add_to_balance(self, value):
        self.balance += value
        return True

    def remove_from_balance(self, value):
        if self.balance >= value:
            self.balance = self.balance - value
            return True
        else:
            return False

