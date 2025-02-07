from enum import Enum


class Acc(Enum):
    OPEN = True
    CLOSED = False


class BankAccount:
    def __init__(self) -> None:
        self.is_open = Acc.CLOSED
        self.transtactions: list[int] = []
        self.balance: int = 0

    def open(self):
        if self.is_open is Acc.OPEN:
            raise ValueError("account already open")
        self.is_open = Acc.OPEN

    def get_balance(self):
        self.ensure_acc_open()
        return self.balance

    def deposit(self, amount):
        self.ensure_acc_open()
        if amount > 0:
            self.transtactions.append(amount)
            self.balance += amount
        else:
            raise ValueError("amount must be greater than 0")

    def withdraw(self, amount):
        self.ensure_acc_open()
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        if self.balance - amount >= 0:
            self.transtactions.append(-1 * amount)
            self.balance -= amount
        else:
            raise ValueError("amount must be less than balance")

    def close(self):
        self.ensure_acc_open()
        self.__init__()

    def ensure_acc_open(self):
        if self.is_open is Acc.CLOSED:
            raise ValueError("account not open")
