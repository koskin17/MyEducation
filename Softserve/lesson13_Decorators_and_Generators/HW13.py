# def add_tag(tag):
#     def decorator(func):
#         def wrapper():
#             result = func()
#             return f"{tag}{result}{tag}"
#         return wrapper
#     return decorator
#
#
# @add_tag("<strong>")
# def get_message():
#     return "Hello, World!"
#
# print(get_message())

# def fibonacci_numbers():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacci_numbers()
# for i in range(10):
#     print(next(fib))
# def celsius_to_fahrenheit(temps):
#     return [(cel_grad * 9/5) + 32 for cel_grad in temps]
#
#
# celsius_temperatures = [0, 10, 20, 30, 40]
# print(celsius_to_fahrenheit(celsius_temperatures))
#
# celsius_temperatures = [-40, -30, -20, -10, 0]
# print(celsius_to_fahrenheit(celsius_temperatures))
# def celsius_to_fahrenheit(temps):
#     return list(map(lambda cell_grad: (cell_grad * 9/5) + 32, temps))
#
# celsius_temperatures = [0, 10, 20, 30, 40]
# print(celsius_to_fahrenheit(celsius_temperatures))
#
# celsius_temperatures = [-40, -30, -20, -10, 0]
# print(celsius_to_fahrenheit(celsius_temperatures))

# def combinations(list1, list2):
#     for el1 in list1:
#         for el2 in list2:
#             yield el1, el2
#
#
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# for combination in combinations(list1, list2):
#     print(combination)

lst1 = [i for i in range(0,5)]
lst2 = [i for i in range(20, 25)]
print([{key: value} for (key, value) in zip(lst1, lst2)])
print({key: value for (key, value) in zip(lst1, lst2)})