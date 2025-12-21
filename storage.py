import json
import pathlib
from user import User

def save_users(path, users):
    emails = [user.email for user in users]

    with open(path, 'w') as plik:
            json.dump(emails, plik, indent=4)


def load_users(path):
    file_path = pathlib.Path(path)
    users = []
    if file_path.exists():
        with open(path, 'r') as plik:
            emails = json.load(plik)
            for email in emails:
                user = User(email)
                users.append(user)
    return users