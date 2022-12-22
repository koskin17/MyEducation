'''
Класс BankAccount имитирует банковский счёт
'''

class BankAccount:
    ''' Метод __init__ принимает аргумент с остатком на счете.
        Он присваивается атрибуту __balance_ '''
    def __init__(self, bal):
        self.__balance = bal

    ''' Метод deposit вносит на счёт вклад '''
    def deposit(self, amount):
        self.__balance += amount

    ''' Метод withdraw снимает сумму со счёта '''
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка: недостаточно средства.')

    ''' Метод get_balance возвращает остаток на счёте '''
    def get_balance(self):
        return self.__balance
        
