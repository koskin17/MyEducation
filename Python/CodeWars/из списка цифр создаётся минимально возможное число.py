def min_value(digits):
    return int(''.join(map(str, sorted(list(set(digits))))))
