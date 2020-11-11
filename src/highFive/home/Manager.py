from .User import User

class Manager(User):
    
    def __init__(self, name, username, password, emailAddress):
        User.__init__(self, name, username, password, emailAddress)


