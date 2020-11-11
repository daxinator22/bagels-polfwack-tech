from .User import User

class Cashier(User):
    
    def __init__(self, name, username, password, emailAddress):
        User.__init__(self, name, username, password, emailAddress)


