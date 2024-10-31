# Практика по property

from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        """
        До этого аттрибут password был с двумя подчеркиваниями.
        Т.е. при инициализации объекта аттрибут passwod сразу становился защищенным и ему
        сразу присваивался пароль без проверок.
        Для того, чтобы проверки выполнялись в момент инициализации экземпляра,
        в качестве собственного (self) имени аттрибута вызывается свойство.
        В нашем случае это свойство password, т.е. без подчеркиваний.
        Т.е. сразу запускается setter, который сразу проверяет пароль на корректность.
        """
        self.password = password
        self.__secret = "Секретные данные"

    # Проверка пароля на наличие цифр.
    # Для того, чтобы self не принимался, вешаем декоратор staticmethod
    @staticmethod
    def is_include_number(password):
        # Для проверки используем метод digits из модуля string
        for digit in digits:
            if digit in password:
                return True

        return False

    # Получение доступа к секретному аттрибуту
    @property
    def secret(self):
        s = input("Введите Ваш пароль: ")
        if s == self.password:
            return self.__secret
        else:
            raise ValueError("Доступ закрыт")

    @property
    # По умолчанию эта функция getter
    def password(self):
        return self.__password

    # Устанавливает свойству метод setter
    @password.setter
    def password(self, value):
        # В setter добавляем проверку и вызываем исключение
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой.")
        if len(value) < 3:
            raise ValueError("Пароль слишком короткий. Минимум 3 символа.")
        if len(value) > 12:
            raise ValueError("Пароль слишком длинный. Максимум 12 символов.")
        # Для проверки пароля на наличие цифр создадим отдельную функцию
        # Перед установкой пароля вызываем метод проверки для пароля
        if not User.is_include_number(value):
            raise ValueError("Пароль должен содержать цифры")

        self.__password = value


"""
Проблема, которая возникает при работе с классом в том, что можно спокойно обращаться к аттрибутам этого
класса, менять аттрибуты и т.д.
В данном случае в password можно сохранить всё, что угодно.
Даже создать объект класса, сохранить в этот пароль.
Но:
- пароль всегда должен быть строкой;
- нужно закрыть доступ к паролю;
- мы должны быть уверены, что пароль безопасный.

Для всего этого и нужно property. С его помощью можно отловить момент, когда к аттрибуту идёт обращение или
попытка его изменить.
Т.е. property отлавливает событие getter и событие setter.
Соответственно, при отлавливании события, на него можно повлиять и, к примеру, запретить.
"""

user1 = User(input("Введите логин: "), input("Введите пароль: "))
print(user1.password)

user1.password = input("Введите новый пароль: ")
print("Новый пароль: ", user1.password)
print(user1.secret)
