"""
You are given a secret message you need to decipher.
Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
"""


def decipher_this(string):
    new_lst = []
    for word in string.split():
        if word.isdigit():
            new_lst.append(chr(int(word)))
        else:
            part1 = word[:3]
            part2 = word[3:]
            if not part1.isdigit():
                part1 = word[:2]
                part2 = word[2:]

            new_word = chr(int(part1)) + part2
            if len(chr(int(part1)) + part2) <= 2:
                new_lst.append(new_word)
            else:
                new_word = new_word[0] + new_word[-1] + new_word[2:-1] + new_word[1]
                new_lst.append(new_word)

    return " ".join(new_lst)


print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
print(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"))
print(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"))
print(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"))
print(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"))
