text = """Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. 
Complex is better than complicated. Flat is better than nested. Sparse is better than dense.
Readability counts. Special cases aren't special enough to break the rules."""
print('Number of occurrence of better:', text.count('better'), 'never:', text.count('never'), 'is:', text.count('is'))
print(" ")
print(text.upper())
print(" ")
replaced_text = text.replace('i', '&')
print(replaced_text)