class UserMail:
    def __init__(self, login, email):
        self.login = login
        self._email = email

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        if isinstance(new_email, str) \
                and new_email.count("@") == 1 \
                and "." in new_email[new_email.index("@") + 1:]:
            print("Почта введена верно.")
            self._email = new_email
        else:
            print(f"ErrorMail: {new_email}")

    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', 'test@mail.com')
print(k.email)
k.email = [1, 2, 3]
k.email = 'test@test@.mail'
k.email = 'new_test@test.com'
print(k.email)
