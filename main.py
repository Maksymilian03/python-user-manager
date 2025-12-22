from user_manager import UserManager
from user import User
from storage import load_users, save_users


# user1 = User('email1@wp.pl')
# user2 = User('email2@wp.pl')
# user3 = User('email3@wp.pl')
# user4 = User('email4@wp.pl')
#
# path = 'plik.json'
#
# uzytkownicy = [user1, user2, user3, user4]
# save_users(path, uzytkownicy)
#
# users = load_users('plik.json')
# for user in users:
#     print(user.email, user.is_valid())

m = UserManager("nowy.json")
m.add_user("kowalski@wp.pl")
m.add_user("nowak@wp.pl")
m.add_user("radzik@wp.pl")
print(m.list_users())
m.save()
m2 = UserManager("nowy.json")
print(m2.list_users())


