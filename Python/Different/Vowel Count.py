def get_count(sentence: str):
    vowels = 0
    for letter in sentence:
        if letter in "aeiou":
            vowels += 1

    return vowels

# Вариант 2
def get_count(sentence: str):
    return sum(c in 'aeiou' for c in s)
