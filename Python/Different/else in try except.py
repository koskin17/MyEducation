# В блоках try / except можно использовать ветку else.
# Она будет выполняться, если не возникло исключение

print("Вариант 1:")
try:
    2 / 'a'
except TypeError:
    print("An exception was raised")
else:
    print("Good! No exception was raised!")

print("Вариант 2:")
try:
    2 * 3
except TypeError:
    print("An exception was raised")
else:
    print("Good! No exception was raised!")
