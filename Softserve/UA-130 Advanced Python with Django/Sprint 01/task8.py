# 's3ooOOooDy' has exams. He wants to study hard this time. He has an array of studying hours per day for the previous exams. He wants to know the length of the maximum non-decreasing contiguous subarray of the studying days, to study as much before his current exams.

# Example:

# For a = [2,2,1,3,4,1] the answer is 3.

# [input] array.integer a

# The number of hours he studied each day.

# [output] integer

# The length of the maximum non-decreasing contiguous subarray.

# У 's3ooooooooDy' экзамены. В этот раз он хочет хорошо учиться. У него есть массив учебных часов в день для предыдущих экзаменов. Он хочет узнать длину максимального неубывающего смежного подмассива учебных дней, чтобы заниматься столько же перед текущими экзаменами.

# Пример:

# Для a = [2,2,1,3,4,1] ответ - 3. [вход] array.integer a Количество часов, которые он занимался каждый день.

# [output] integer Длина максимального неубывающего смежного подмассива.
def max_non_decreasing_subarray(a):
    max_length = 1
    current_length = 1
    
    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:  # Проверяем, идет ли последовательность вверх или на одном уровне
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1  # Начинаем новую последовательность
    
    return max(max_length, current_length)

# Пример использования:
a = [2, 2, 1, 3, 4, 1]
print(max_non_decreasing_subarray(a))  # Ожидаемый вывод: 3

# Как работает код?
# 1️⃣ current_length отслеживает длину текущего непрерывного участка.
# 2️⃣ Если следующий элемент не меньше предыдущего, увеличиваем current_length.
# 3️⃣ Если обнаружен спад (a[i] < a[i-1]), обновляем max_length и начинаем новую последовательность.
# 4️⃣ В конце возвращаем максимальную найденную длину.
# Это O(n)-алгоритм — он проходит список всего один раз и быстро находит ответ! 🚀
# Попробуй запустить и скажи, если что-то не так! 😃
