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




