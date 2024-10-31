"""
Task
Given a string str, reverse it and omit all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".
"""


def reverse_letter(string: str):
    tmp_str = ""
    for letter in string:
        if letter.isalpha():
            tmp_str += letter

    return tmp_str[::-1]

# Вариант 2
def reverse_letter2(s):
  return ''.join([i for i in s if i.isalpha()])[::-1]

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))
print(reverse_letter("ab23c"))
print(reverse_letter("krish21an"))
