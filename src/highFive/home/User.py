class User:
    
    def __init__(self, name, username, password, emailAddress):
        self.name = name
        self.username = username
        self.password = password
        self.emailAddress = emailAddress

    def printName(self):
        print(f'My name is {self.name}, my username is {self.username} and my password is {self.password}')
