import os
from user import User

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    self.users[username] = User(username, password)

    def login(self, username, password):
        return username in self.users and self.users[username].password == password

    def register(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            self.save_users()
            return True
        return False

    def save_users(self):
        with open("users.txt", "w") as file:
            for user in self.users.values():
                file.write(f"{user.username},{user.password}\n")
