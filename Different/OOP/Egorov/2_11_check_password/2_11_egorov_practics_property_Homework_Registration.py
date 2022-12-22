import string
from string import *


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not value.count("@") == 1:
            raise ValueError("Login must include at least one '@'")
        if not value.count(".") == 1:
            raise ValueError("Login must include at least one '.'")
        self.__login = value

    @staticmethod
    def is_include_all_register(password):
        upper_letter = 0
        for digit in password:
            if digit.isupper():
                upper_letter += 1
        return upper_letter

    @staticmethod
    def is_include_digit(password):
        for digit in password:
            if digit in digits:
                return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        for digit in password:
            if digit.isalpha() and digit not in string.ascii_letters:
                return False
        return True

    @staticmethod
    def check_password_dictionary(password):
        tmp_lst = []
        with open('easy_passwords.txt', 'r') as file:
            for line in file:
                tmp_lst.append(line.strip('\n'))

            for value in tmp_lst:
                if password == value:
                    return False

        return True

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise ValueError("Password must be a string.")
        if not 3 < len(password) < 13:
            raise ValueError("Len of the password must be between 4 and 12 symbols.")
        if not Registration.is_include_digit(password):
            raise ValueError("Password must include at least one figure.")
        if Registration.is_include_all_register(password) < 2:
            print(Registration.is_include_all_register(password))
            raise ValueError("Password must include at least 2 letter in upper case.")
        if not Registration.is_include_only_latin(password):
            raise ValueError("Password must include only latin alphabet.")
        if not Registration.check_password_dictionary(password):
            raise ValueError("Your password is too easy.")

        print("Password is good!")
        self.__password = password


t1 = Registration("test@test.com", "PAssword123")
