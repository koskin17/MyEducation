def find_odd(lst):
    counts={k: lst.count(k) for k in set(lst)}
    # Створюємо список чисел, що з'являються непарну кількість разів
    odd_occurrences = []
    # for element in counts.items():
    #     if element[0] % 2 != 0:
    #         odd_occurrences.append(element[1])
    # return odd_occurrences

    for k in counts:
        if k % 2 != 0:
            odd_occurrences.append(counts[k])
    return odd_occurrences

print()