from user import User
from storage import load_users, save_users

class UserManager:
    def __init__(self, path):
        self.path = path
        self.users = load_users(path)

    def list_users(self):
        list_users = [user.email for user in self.users]
        return list_users

    def add_user(self, email):
        if email in self.list_users():
            return False
        else:
            user = User(email)
            if user.is_valid():
                self.users.append(user)
                return True
        return False

    def save(self):
        save_users(self.path, self.users)

    def remove_user(self, user_email):
        if user_email in self.list_users():
            for user in self.users:
                if user.email == user_email:
                    self.users.remove(user)
                    return True
        return False




