# Метод фильтрации списка от значений
def filter_lst(lst):
    return list(filter(None, lst))


print(filter_lst([0, 1, False, None, 2, '', 3, 'a', 's', 34]))
# 0, False, None, пустая строка '' - являются None
