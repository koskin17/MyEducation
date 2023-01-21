"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.
"""


def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstivwxyz"
    return True if all(i in s.lower() for i in alphabet) else False


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))
