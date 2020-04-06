import time

# Base class definition
class Account:

    def __init__(self, name, balance, account_number, username, password, phone_number, account_type, min_balance):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.account_type = account_type
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough money.")

    def statement(self):
        print(" You have ${} in your bank account.".format(self.balance))


# Subclass definitions
class Checking(Account):

    def __init__(self, name, balance, account_number, username, password, phone_number, account_type, min_balance):
        super().__init__(name, balance, account_number, username,
                         password, phone_number, account_type, min_balance=-1000)


class Savings(Account):

    def __init__(self, name, balance, account_number, username, password, phone_number, account_type, min_balance, creation_time):
        super().__init__(name, balance, account_number, username,
                         password, phone_number, account_type, min_balance=0)
        self.creation_time = creation_time

    def pay_interest(self):
        y_difference = time.localtime().tm_year - self.creation_time[0]
        some_months = y_difference * 12
        more_months = time.localtime().tm_mon - self.creation_time[1]
        months = some_months + more_months
        i = 0
        while i < months:
            amount = (self.balance * .01)/12
            self.balance += amount
            i += 1