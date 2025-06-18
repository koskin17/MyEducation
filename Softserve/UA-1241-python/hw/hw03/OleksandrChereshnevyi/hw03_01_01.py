zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


zen_list = zen.replace('.',' ').upper().split()

count_better, count_never, count_is = 0, 0, 0

for i in range(len(zen_list)):
    if (str(zen_list[i]) == "BETTER"):
        count_better += 1
    if (str(zen_list[i]) == "NEVER"):
        count_never += 1
    if (str(zen_list[i]) == "IS"):
        count_is += 1

print("\n1. The number of occurrences of the words better, never and is:")
print(f"{count_better=}, {count_never=}, {count_is=}")

print("\n2. Display all text in uppercase (all letters in uppercase):")
print(zen.upper())

print("\n3. Replace all occurrences of the symbol “i” with “&”:")
print(zen.replace('i', '&'))