# Получение наиболее часто повторяющегося символа в последовательности

def most_frequent(nums):
    return max(set(nums), key=nums.count)


nums = [1, 4, 5, 6, 4, 589, 6, 5, 4, 55, 8, 4, 6, 22, 4, 5, 6]
print(most_frequent(nums))