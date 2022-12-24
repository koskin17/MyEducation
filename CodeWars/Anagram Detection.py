# write the function is_anagram
def is_anagram(test, original):
    tmp1 = []
    for letter in test.lower():
        tmp1.append(letter)

    tmp2 = []
    for letter in original.lower():
        tmp2.append(letter)
    return sorted(tmp1) == sorted(tmp2)

def is_anagram2(test, original):
    return sorted(original.lower()) == sorted(test.lower())


print(is_anagram("Buckethead", "DeathCubeK"))
print(is_anagram2("Buckethead", "DeathCubeK"))
