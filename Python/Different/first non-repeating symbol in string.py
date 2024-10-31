"""
⚡️ Задача: найдите первый неповторяющийся символ в строке, выполнив только один обход

Для заданной строки найдите в ней первый неповторяющийся символ, выполнив только один ее обход.

Например,

Input:

string is ABCDBAGHC

Output:

первый неповторяющийся символ: D
"""
from collections import Counter


s = "AABBCCDDAGHC"
# lst = Counter(s)
# print(lst)
for key, value in Counter(s).items():
    if value == 1:
        print(key)
        break