"""
https://t.me/c/1570297240/568
Make the string great AGAIN
Сложность: Лёгкая

Условие задачи: дается строка, состоящая из латинских букв как в нижнем, так и в вернем регистре.

Строка считается качественной, если две соседние буквы не представлены одной и той же буквой, но в разных регистрах.
Такие буквы удаляются до тех пор, пока строка не станет качественной.
Вернуть надо строку, над которой были совершены все преобразования. Гарантируется уникальность ответа.
Пустая строка по умолчанию является качественной.

Пример:
Ввод: s = "leEeetcode"
Вывод: "leetcode"
"""


def great_string(s):
    result = []
    for c in s:
        if not result:
            result.append(s)
        elif result[-1].isupper() and result[-1].lower() == c:
            result.pop()
        elif result[-1].islower() and result[-1].upper() == c:
            result.pop()
        else:
            result.append(c)

    return ''.join(result)


print(great_string("leEeetcode"))
