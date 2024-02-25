from abc import ABC, abstractmethod

class LoginMethod(ABC):
    @abstractmethod

    def authorize(self, username, password):
        "No Payment Method specified"

class logging(LoginMethod):
    def __init__(self):
        self.usernames = ["user1", "user2", "user3"]
        self.passwords = ["password1", "password2", "password3"]

    def authorize (self, username, password):
        if username in self.usernames and password in self.passwords:
            print(f"User {username} logged in")
        else:
            print("Invalid credentials")

class loguru(LoginMethod):
    def __init__(self):
        self.usernames = ["user1", "user2", "user3"]
        self.passwords = ["password1", "password2", "password3"]

    def authorize (self, username, password):
        if username in self.usernames and password in self.passwords:
            print(f"User {username} logged in")
        else:
            print("Invalid credentials")
    
class Google_auth(LoginMethod):
    def __init__(self):
        self.usernames = ["user1", "user2", "user3"]
        self.passwords = ["password1", "password2", "password3"]

    def authorize (self, username, password):
        if username in self.usernames and password in self.passwords:
            print(f"User {username} logged in")
        else:
            print("Invalid credentials")

class LoginAuth:
    def __init__(self, LoginAuth: LoginMethod):
        self.login_method = LoginMethod

    def process_payment(self, username, password):
        self.login_method.authorize(username, password)


if __name__ == "__main__":
    login = logging()
    login.authorize("user1", "password1")
    login = loguru()
    login.authorize("user1", "password1")
    login = Google_auth()
    login.authorize("user1", "password1")