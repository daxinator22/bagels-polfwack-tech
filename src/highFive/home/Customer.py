from .User import User

class Customer(User):
    
    def __init__(self, name, username, password, emailAddress, balance, orders):
        User.__init__(self, name, username, password, emailAddress)
        self.balance = balance
        self.orders = orders


