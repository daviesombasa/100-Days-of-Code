"""
#100 Days of Code Challenge
Day 10: Classes: Objected Oriented Programming
Note:
    1. To execute a block of code use Alt + Shift + E on Pycharm IDE
    2. Classes have two types of variables:
        i. Class variables - globally declared within the class
            - do not change during execution
        ii. Instance variables - declares within a method
            - can change with each execution of the class
    3. Classes are comprised of methods which are basically functions
"""


class Account:
    def __init__(self):
        self.acc_interest = 0
        self.acc_type = None
        self.acc_number = None
        self.acc_balance = None

    def details(self):
        return f"Acc Number: {self.acc_number} \n" \
               f"Acc Balance: {self.acc_balance}"

    def account_type(self):
        if str(self.acc_number).startswith('1'):
            self.acc_type = 'current'
        elif str(self.acc_number).startswith('2'):
            self.acc_type = 'savings'
        return f"Acc type: {self.acc_type}"

    def interest_rate(self):
        self.account_type()
        if self.acc_type == 'current':
            self.acc_interest = 10
        elif self.acc_type == 'savings':
            self.acc_interest = 15
        return f"Acc interest: {self.acc_interest}"

    def interest_amount(self):
        self.interest_rate()
        return f"Interest amount: {(self.acc_interest / 100) * self.acc_balance}"


if __name__ == "__main__":
    acc_number = int(input('Enter you account number: '))
    acc_balance = int(input('Enter your account balance: '))
    client = Account()
    client.acc_number = acc_number
    client.acc_balance = acc_balance
    print(client.details())
    print(client.account_type())
    print(client.interest_rate())
    print(client.interest_amount())

