# Property и методы getters и setters

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        # Для того, чтобы передаваемое значение было чиcлом, т.е. экземпляром числа,
        # перед установкой в методе setter добавляется проверка принадлежности value
        # к типу данных int и float.
        # В противном случае вызывается исключение с сообщением
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        else:
            self.__balance = value

    # При использовании методов getter и setter в коде нужно их вызывать
    # Для того, чтобы упростить задачу и получать доступ к защищенным атрибутам, а также
    # устанавливать им новые значения используется своёство Property
    # Для этого внутри класса создаётся имя свойства и внутри проставляются 2 аттрибута
    # fget (getter) и fset (setter) и в качестве значений этих атрибутов указываются именя методов

    # Аналогично добавляется метод удаления аттрибута. Создаётся функция, а в свойство добавляется fdel с
    # указанием имени метода
    def delete_balance(self):
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
    # Цей код створює **властивість** (property) у класі Python, яка називається `balance`.
    # ---
    # ### 🔍 Що таке `property`?
    # `property` — це спеціальний механізм у Python, який дозволяє **звертатися до методів як до звичайних змінних**. Він використовується для **інкапсуляції** — коли ми хочемо контролювати доступ до атрибутів (наприклад, перевіряти або змінювати значення тільки за певними правилами).
    # ---
    # ### 🔧 У твоєму прикладі:
    # * `fget=get_balance` — функція (метод), яка буде викликатись, коли ти звертаєшся до `balance`
    # * `fset=set_balance` — функція, яка буде викликатись, коли ти ПРИСВОЮЄШ значення `balance`
    # * `fdel=delete_balance` — функція, яка буде викликатись, коли ти ВИДАЛЯЄШ `balance`
    # ---
    # ### 🔍 Приклад для розуміння:
    # ```python
    # class Account:
    #     def __init__(self):
    #         self._balance = 0  # приватна змінна

    #     def get_balance(self):
    #         print("Отримуємо баланс...")
    #         return self._balance

    #     def set_balance(self, value):
    #         print("Встановлюємо баланс...")
    #         if value < 0:
    #             raise ValueError("Баланс не може бути від'ємним!")
    #         self._balance = value

    #     def delete_balance(self):
    #         print("Видаляємо баланс...")
    #         del self._balance

    #     balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
    # ```
    # ---
    # Тепер, коли ти звертаєшся до `balance`, Python автоматично викликає відповідні методи:
    # ### 🧪 Як це працює:
    # ```python
    # acc = Account()
    # acc.balance = 100     # викликається set_balance
    # print(acc.balance)    # викликається get_balance
    # del acc.balance       # викликається delete_balance
    # ```
    # 🔁 За кулісами Python перетворює звернення до `balance` на виклики методів.
    # ---
    # ### ✅ Простими словами:
    # > `balance = property(...)` — це спосіб зробити змінну `balance` розумною: коли ти читаєш, записуєш або видаляєш її, викликаються спеціальні функції.
    # Це зручно, коли ти хочеш:
    # * перевіряти або змінювати значення перед тим, як його зберегти;
    # * заборонити встановлювати некоректні значення;
    # * логувати звернення до змінної.


client1 = BankAccount('Ivan', 1000)
client2 = BankAccount('Misha', 2000)

# И теперь нам доступно имя balance, но оно не атрибут экземпляра, а свойство
# И при обращении к нему (без круглых скобочек) срабатывает метод get_balance - getter
# Этот метод возвращает защищенный атрибут balance

print(f"Клиент {client1.name} с балансом:", client1.balance)
print(f"Клиент {client2.name} с балансом:", client2.balance)

# И установка нового значения также происходит обращением к свойству balance
client1.balance = 1500
client2.balance = 1500
print(f"Клиент {client1.name} с новым балансом:", client1.balance)
print(f"Клиент {client2.name} с новым балансом:", client2.balance)
del client1.balance
del client2.balance
# После удаления баланса у клиентов такого свойства, как balance, уже нет

