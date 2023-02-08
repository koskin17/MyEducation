import datetime

# Метод 1
start = datetime.datetime.now()
"""Some code"""
print(datetime.datetime.now() - start)

# Метод 2
import time

start_time = time.time()
"""Some code"""
print(f"Total time to execute code is {(time.time() - start_time)}")

# Метод 3
import timeit
code = [2,3,6,5,8,9,15,14,18,19,54,36,98].sort()
print(timeit.timeit(stmy=code, number=1000))
