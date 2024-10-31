"""
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
"""
def order(sentence):
    tmp_lst = []
    for word in sentence.split():
        for letter in word:
            if letter.isdigit():
                tmp_lst.append([letter, word])

    tmp_lst2 = []
    for word in sorted(tmp_lst):
        tmp_lst2.append(word[1])

    return " ".join(tmp_lst2)


print(order("is2 Thi1s T4est 3a")) #, "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"))# , "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""))# , "")
