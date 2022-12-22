class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # def get_balance(self):
    #     return self.__balance

    # def set_balance(self, value):
    #     if not isinstance(value, (int, float)):
    #         raise ValueError("Баланс должен быть числом")
    #     else:
    #         self.__balance = value
    #
    # def delete_balance(self):
    #     del self.__balance

    # Свойство property сразу имеет методы setter, getter и delete.
    # Т.е. можно сразу назвать свойство, присвоить его классу Property() и вызывать эти методы.
    # При этом при назначении property можно сразу передавать метод getter
    # my_balance = property(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)

    # Также свойство property можно использовать в качестве декоратора,
    # что заменяет строку кода my_balance = property(get_balance)
    @property
    def my_balance(self):
        return self.__balance
