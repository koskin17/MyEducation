def fibonacci_up_to_n(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

fibonacci_up_to_n(13) # 0 1 1 2 3 5 8 13