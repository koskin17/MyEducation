l = [1, "a", "b", 0, 15]

new_list = []


def filter_list(l):
    for i in range(len(l)):
        if type(l[i]) == type(2):
            new_list.append(l[i])
    return new_list

print(filter_list(l))
