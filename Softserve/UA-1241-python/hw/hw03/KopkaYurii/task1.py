zenPy = """Beautiful is better than ugly.
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

better_count = zenPy.count("better")
never_count = zenPy.count("never")
is_count = zenPy.count("is")

zen_upper = zenPy.upper()

zen_replaced = zen_upper.replace("I", "&")

# Результати
print(f"Occurrences of 'better': {better_count}")
print(f"Occurrences of 'never': {never_count}")
print(f"Occurrences of 'is': {is_count}")
print("\nText in uppercase:\n")
print(zen_upper)
print("\nText with 'I' replaced by '&':\n")
print(zen_replaced)
