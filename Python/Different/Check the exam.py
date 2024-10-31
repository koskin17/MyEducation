"""
The two arrays are not empty and are the same length. Return the score for this array of answers,
giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer,
represented as an empty string (in C the space character is used).

If the score < 0, return 0.

For example:

checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
"""


def check_exam(arr1, arr2):
    score = 0
    for answer1, answer2 in zip(arr1, arr2):
        if answer1 == "" or answer2 == "":
            score += 0
        elif answer1 == answer2:
            score += 4
        else:
            score -= 1
    return score if score > 0 else 0


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]))
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))
print(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]))
