''' Из полученного списка, в котором повторяются элементы, нужно вывести список уникальных элементов, т.е. по одному разу каждый, в тот порядке, в котором они были.
Также важно проверить список на пустоту'''

iterable = 'AAAABBBCCDAABBB'

def unique_in_order(iterable):
    new_list = []
    if not iterable:                                        # проверка полученного списка на его пустоту
        return new_list
    else:
        new_list.append(iterable[0])
        for symbol in range(1, len(iterable)):
            if iterable[symbol] == iterable[symbol-1]:
                            continue
            else:
                new_list.append(iterable[symbol])
    return new_list

                        
print(unique_in_order(iterable))
