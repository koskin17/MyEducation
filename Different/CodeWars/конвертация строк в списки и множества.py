example_string = 'Привет! Это просто тестовая строка, которую я хочу попробовать сделать списком.'
example_list = example_string.split(' ')
print(example_list)
print('Итерация полученного списка циклом for')
for i in example_list:
    print(i)

example_string_for_set = ('А а это это строка строка строка, которую которую я я хочу попробовать попробовать переделать переделать во множество.')
example_list_2 = example_string_for_set.split(' ')
print(example_list_2)
example_set = set(example_list_2)
print(example_set)
