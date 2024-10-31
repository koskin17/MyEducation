arr = input('Введите набор чисел: ')

def sum_array(arr):
    summ = 0
    for number in arr:
        if number != max(arr) and number != min(arr):
            summ += int(number)
    return summ

print(sum_array(arr))
