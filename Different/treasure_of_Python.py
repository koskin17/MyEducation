# https://telegra.ph/Skrytye-sokrovishcha-Python-01-12

# Атрибуты функции
def func(x):
    var = x**2 + x + 1

    if var % 2:
        print("Число было нечётное.")
    else:
        print("Число было чётное.")

    # установка атрибутов в функции
    func.optional_return = var
    func.is_awesome = "Mu func is awesome!"

    return var


y = func(3)
print("В результате работы функции получилось: ", y)
# Получаем атрибуты функции
print("Результат вычисления в функции: ", func.optional_return)
print(func.is_awesome)
