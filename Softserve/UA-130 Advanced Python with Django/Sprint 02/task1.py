# As input data, you have a list of strings.

# Write a method double_string() for counting the number of strings from the list, represented in the form of the concatenation of two strings from this arguments  list

# For example:

# Тест	Result
# data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
# print(double_string(data))
# 3
# data = ['aa', 'abc', 'qwerqwer']
# print(double_string(data))
# 0
def double_string(data):
    set_word_from_data = set(data)  # Преобразуем список в множество для быстрого поиска O(1)
    counter = 0

    for word in data:
        # Проверяем, можно ли представить слово в виде двух других слов из списка
        for i in range(1, len(word)):  # Начинаем с 1, чтобы избежать пустых подстрок
            prefix, suffix = word[:i], word[i:]
            if prefix in set_word_from_data and suffix in set_word_from_data:
                counter += 1
                break  # Если нашли подходящее разбиение, переходим к следующему слову

    return counter

# Тестовые примеры:
data1 = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data1))  # Вывод: 3

data2 = ['aa', 'abc', 'qwerqwer']
print(double_string(data2))  # Вывод: 0

# Объяснение кода:
# - Создаём множество set_word_from_data из списка слов. Это позволяет быстро проверять, существует ли слово в списке (поиск в множестве занимает O(1)).
# - Перебираем каждое слово в списке.
# - Пробуем разделить слово на две части (prefix и suffix).
# - Проверяем, существуют ли обе части в исходном списке. Если да — увеличиваем счётчик.
# - Если нашли хотя бы одно корректное разбиение, прерываем дальнейшую проверку этого слова и переходим к следующему.
# - Возвращаем итоговый счётчик слов, которые можно представить в виде конкатенации двух других.

# Этот алгоритм работает за O(N * M), где:
# - N — количество слов в списке.
# - M — средняя длина слов.
