from user import User
from storage import load_users, save_users


user1 = User('email1@wp.pl')
user2 = User('email2@wp.pl')
user3 = User('email3@wp.pl')
user4 = User('email4@wp.pl')

path = 'plik.json'

uzytkownicy = [user1, user2, user3, user4]
save_users(path, uzytkownicy)

users = load_users('plik.json')
for user in users:
    print(user.email, user.is_valid())


assert len(users) == 4
assert users[0].email == 'email1@wp.pl'
assert all(user.is_valid() for user in users)