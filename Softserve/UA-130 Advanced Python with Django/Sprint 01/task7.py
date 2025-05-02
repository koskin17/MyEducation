# Nicky and Dev work in a company where each member is given his income in the form of points. On Nicky's birthday, Dev decided to give some of his points as a gift. The number of points Dev is gifting is the total number of visible zeros visible in the string representation of the N points he received this month.

# Let's say that Nicky got M points from Dev. By the company law, if M is even and greater than 0, Nicky must give one point to the company. If M is odd, the company gives Nicky one additional point.

# Given the number of points N Dev received this month, calculate the number of points Nicky will receive as a gift and return this number in its binary form.

# Note: visible zeros are calculated as follows:

# 0, 6 and 9 contain 1 visible zero each;
# 8 contains 2 visible zeros;
# other digits do not contain visible zeros.
# Example

# For N = "565", the output should be
# Cipher_Zeroes(N) = 10.

# There's one visible zero in "565". Since one is odd, the company will give an additional point, so Nicky will receive 2 points.
# 210 = 102, so the output should be 10.

# Input/Output

# [input] string N

# The number of points Dev received this month.

# Constraints:
# 1 ≤ N ≤ 101000.

# [output] integer

# The number of points Nicky will receive in the binary representation.

# Ники и Дев работают в компании, где каждый сотрудник получает свой доход в виде баллов. В день рождения Ники Дев решил подарить часть своих баллов. Количество баллов, которые Дев дарит, - это общее количество видимых нулей в строковом представлении N баллов, которые он получил в этом месяце.

# Предположим, что Ники получил от Дэва M баллов. По закону компании, если M четное и больше 0, Ники должен отдать компании одно очко. Если M нечетное, компания дарит Ники еще одно очко.

# Учитывая количество баллов N Dev, полученных в этом месяце, вычислите количество баллов, которые Ники получит в подарок, и верните это число в двоичном виде.

# Примечание: видимые нули вычисляются следующим образом:

# 0, 6 и 9 содержат по 1 видимому нулю; 8 содержит 2 видимых нуля; остальные цифры не содержат видимых нулей.
# Пример Для N = "565" вывод должен быть Cipher_Zeroes(N) = 10.

# В числе "565" есть один видимый ноль. Поскольку единица нечетная, компания даст дополнительное очко, поэтому Ники получит 2 очка.
# 210 = 102, поэтому на выходе должно получиться 10.

# Ввод/вывод [input] string N Количество баллов, полученных Dev в этом месяце.

# Ограничения:
# 1 ≤ N ≤ 101000.

# [output] целое число Количество очков, которые получит Ники в двоичном представлении.

def Cipher_Zeroes(N):
    zero_count = sum({'0': 1, '6': 1, '9': 1, '8': 2}.get(digit, 0) for digit in str(N)) # на всякий случай перевод передаваемую строку в str на случай, если вдруг будет передано число в формате int

    # Корпоративные правила
    if zero_count > 0 and zero_count % 2 == 0:
        zero_count -= 1
    elif zero_count % 2 == 1:
        zero_count += 1
    
    # Возвращаем двоичное представление
    return bin(zero_count)[2:]

# Примеры:
print(Cipher_Zeroes("565"))  # Ожидаемый вывод: "10"
print(Cipher_Zeroes("8096")) # Ожидаемый вывод: "100"
print(Cipher_Zeroes("888"))  # Ожидаемый вывод: "110"

# ✨ Разбор кода:
# 1️⃣ Используем словарь (dict), чтобы быстро получить количество видимых нулей для каждого символа.
# 2️⃣ Считаем сумму по всем цифрам в N.
# 3️⃣ Применяем условия компании.
# 4️⃣ Конвертируем результат в бинарную систему с помощью bin(M)[2:].
# Этот метод работает эффективно даже для больших значений N, так как использует линейный проход по строке! 🚀

