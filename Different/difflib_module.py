import difflib


lst = ['vasiliy', 'sasha', 'vasyan', 'barbara', 'r']
print(difflib.get_close_matches('vasya', lst, n=2))
