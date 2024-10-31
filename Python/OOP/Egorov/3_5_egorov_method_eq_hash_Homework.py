# Чтобы не реализовывать все магические методы сравнения, можно использовать декоратор functools.total_ordering,
# который позволяет сократить код и реализовать только методы __eq__ и __lt__

from functools import total_ordering


@total_ordering
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


# Декоратор позволил реализовать все методы сравнения для класса Account
acc1 = Account(10)
acc2 = Account(20)
print(acc1 > acc2)
print(acc1 < acc2)
print(acc1 == acc2)
print(acc1 != acc2)
print(acc1 >= acc2)
print(acc1 <= acc2)
