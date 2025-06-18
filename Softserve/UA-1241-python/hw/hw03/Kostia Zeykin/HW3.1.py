""" Part 1 of homework """

count_better = 0
count_never = 0
count_is = 0

s1 = ("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. "
      "Complex is better than complicated. Flat is better than nested. Sparse is better than dense."
      "Readability counts. Special cases aren't special enough to break the rules."
      "Although practicality beats purity."
      "Errors should never pass silently. Unless explicitly silenced."
      "In the face of ambiguity, refuse the temptation to guess."
      "There should be one-- and preferably only one --obvious way to do it."
      "Although that way may not be obvious at first unless you're Dutch."
      "Now is better than never. Although never is often better than *right* now."
      "If the implementation is hard to explain, it's a bad idea."
      "If the implementation is easy to explain, it may be a good idea."
      "Namespaces are one honking great idea -- let's do more of those!")

s1_temp = s1.replace(".", " ").lower()
s1_temp = s1_temp.split(" ")

for i in s1_temp:
    if i == "better":
        count_better += 1
    if i == "never":
        count_never += 1
    if i == "is":
        count_is += 1

print(f"\"Better\" встречается в тесте {count_better} раз(а).")
print(f"\"Never\" встречается в тексте {count_never} раз(а).")
print(f"\"is\" встречается в тексте {count_is} раз(а).")
print(f"Вариант строки в Uppercase: {s1.upper()}")
print(f"Строки с заменой всех \"i\" на \"&\": {s1.replace("i", "&")}")


""" Part 2 of homework """
s2 = input("Введите 4-е числа через запятую: ")
s2 = s2.replace(" ", "")
s2 = s2.split(",")
s2_temp = []

product = 1

for i in s2:
    if not int(i):
        pass
    else:
        product *= int(i)
        s2_temp.append(int(i))

print(f"Произведение всех введённых числе равно: {product}")
print(f"Числа в порядке убывания: {sorted(s2_temp, reverse=True)}")
print(f"Числа в порядке возрастания: {sorted(s2_temp, reverse=False)}")

""" Part 3 of homework """
var1 = 1
var2 = 2
print(f"Переменная var1 равна: {var1}")
print(f"Переменная var2 равна: {var2}")
var2, var1 = var1, var2
print(f"После смены значений переменных местами переменная var1 равна {var1}, а переменная var2 равна {var2}")
