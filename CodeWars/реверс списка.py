lst = [1,2,3,4]

def reverse_list(lst):
    if lst == []:
        return []
    else: lst.reverse()
    return lst

print(reverse_list(lst))

''' Второй вариант.
В нём список отображается с шагом -1, т.е. в обратном
направление и не важно, пустой или нет список'''
def reverse_list(lst):
    return lst[::-1]
