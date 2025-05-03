# Given two permutations p and q of length n. Find a permutation r, such that for every 1 <= i <= n, q[i] = p[r[i]].

# Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.

# Example

# Input:
# p = [5, 1, 3],  q = [3, 1, 5]

# Output:
# r = [3, 2, 1]
# [input] array.integer p

# [input] array.integer q

# [output] array.integer

# permutation r

# Нам нужно найти такую перестановку r, чтобы для каждого индекса i выполнялось условие:
# q[i] = p[r[i]]
# Поскольку p и q — перестановки длины n (то есть содержат все числа от 1 до n без повторений), каждое число встречается ровно один раз. Это позволяет нам создать словарь, в котором для каждого значения из p сохранён его индекс (с учётом 1-индексации). Затем, для каждого элемента из q находим соответствующий индекс из p.

def find_permutation_r(p, q):
    # Создаем словарь, где ключ - значение из p,
    # а значение - его индекс (1-indexed)
    index_map = {value: i + 1 for i, value in enumerate(p)}
    
    # Для каждого элемента x в q находим индекс его появления в p.
    r = [index_map[x] for x in q]
    
    return r

# Пример:
p = [5, 1, 3]
q = [3, 1, 5]
r = find_permutation_r(p, q)
print(r)  # Ожидаемый вывод: [3, 2, 1]