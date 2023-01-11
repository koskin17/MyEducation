"""
Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step (inclusive).

If begin value is greater than the end, function should returns 0

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
"""


def sequence_sum(begin_number, end_number, step):
    return sum(number for number in range(begin_number, end_number + 1, step)) if begin_number <= end_number else 0


print(sequence_sum(2, 2, 2))


# Можно без условия - если старт в range больше end, то последовательность будет равна 0и сумму равна 0
def sequence_sum2(begin_number, end_number, step):
    return sum(number for number in range(begin_number, end_number + 1, step))


print(sequence_sum2(2, 2, 2))
