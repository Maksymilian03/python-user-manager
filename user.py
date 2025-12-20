class User:
    def __init__(self, email):
         self.email = email

    def is_valid(self):
        if " " in self.email:
            return False

        if self.email.count('@') != 1:
            return False

        email_left, email_right = self.email.split('@')

        if len(email_left) == 0 or len(email_right) == 0:
            return False

        if '.' not in email_right:
            return False

        else:
            return True



User1 = User("a@b.com")
User2 = User("ab.com")
User3 = User("a@@b.com")
User4 = User("a@b")
User5 = User("a @b.com")

print(User1.is_valid())
print(User2.is_valid())
print(User3.is_valid())
print(User4.is_valid())
print(User5.is_valid())



