'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

x = 'letters will be lowercase and'

def high(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    scores = {}
    for word in x.split():
        index = 0
        for letter in word:
            index += alphabet.index(letter)+1
        scores.setdefault(index, word)
    return scores.get(max(scores.keys()))

print(high(x))
