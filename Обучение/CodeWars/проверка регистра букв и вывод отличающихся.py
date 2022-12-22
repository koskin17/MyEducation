'''
DESCRIPTION:
Your task is very simple. Given an input string s, case_sensitive(s), check whether all letters are lowercase or not. Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.

For example, case_sensitive('codewars') returns [True, []], but case_sensitive('codeWaRs') returns [False, ['W', 'R']].
'''

s = 'absDbuY'

def case_sensitive(s):
    wrong_letter = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if s == []:
        return [True, []]
    if s.isupper() or s.islower():
        return [True, wrong_letter]
    else:
        for letter in s:
            if letter not in alphabet:
                wrong_letter.append(letter)
    return [False, wrong_letter]

print(case_sensitive(s))
