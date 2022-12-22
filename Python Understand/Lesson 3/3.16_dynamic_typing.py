# Динамическая типизация

def multiplay(number_1, number_2):
    print("Функцию вызвали с параметрами: ", number_1, number_2)
    # Настоятельно рекомендуется всегда проверять передаваемые в функцию параметры
    if isinstance(number_1, int) and isinstance(number_2, int):
        value = number_1 * number_2
        return value

    return "Ошибка в переданных параметрах"


def elephant_to_free(some_list):
    if isinstance(some_list, list):
        elephant_found = 'elephant' in some_list
        if elephant_found:
            some_list.remove('elephant')
            return "Слон выпущен на свободу."
        else:
            return "Слона в зоопарке нет."

    return "Кортеж - неизменяемый типа данных"


# В функцию переменную из внешней программы можно передавать в изменённом виде.
# Допустим есть список:
zoo = ['lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant']
# При вызове функции и передаче в неё этого списка можно указать новый тип списка.
# Например, кортеж
test1 = elephant_to_free(some_list=zoo)
print(test1)
test2 = elephant_to_free(some_list=tuple(zoo))
# В этом случае список zoo станет кортежем zoo и его уже изменить внутри функции нельзя
print(test2)
