#list 

# l = []
# print(type(l), l)

# l = [1,2,"test", None, [1,2], 3.5]
# print(type(l), l)

# l = list()
# print(type(l), l)

# # l = list(1)#TypeError: 'int' object is not iterable
# l = list("test")
# print(type(l), l)


# l = [1,2,"test", None, [1,2], 3.5]

# print(l[1])
# print(l[2][3])
# print(l[2:5])
# print(l[2:5][0])
# print(l[::2])
# print(l[-1])
# print(l[-2])
# l[1] = (1,2,3)
# print(l)

# print([1,2,3] + [1,2,3])

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = l1 + l2
# print(id(l1), l1)
# print(id(l2), l2)
# print(id(l3), l3)
# print(l1*3)

# l = [1,2,"test", None, [1,2,3], 3.5]
# print([1,2,3] in l)
# print(3 in l)


# l1 = [1,2,3]
# l2 = [1,2,3]
# print(l1 == l2)

# l1 = [1,2,3]
# l2 = [1,3,2]
# print(l1 == l2)

# # print([method for method in dir(list)])
# print([method for method in dir(list) if not method.startswith("_")])

# # l = []
# # print(id(l), l)
# # l.append(1)
# # print(id(l), l)
# # l.append([1,2,3,4])
# # print(id(l), l)
# # l.clear()
# # print(id(l), l)
# # l = []
# # print(id(l), l)

# l = [1,2,"test", None, [1,2,3], 3.5]
# # lc = l.copy() #l[:]
# # print(id(l), l)
# # print(id(lc), lc)
# # l[4][0] = "Foo"
# # print(id(l), l)
# # print(id(lc), lc)
# # from copy import deepcopy

# # l = [1,2,"test", None, [1,2,3], 3.5]
# # lc = deepcopy(l)
# # print(id(l), l)
# # print(id(lc), lc)
# # l[4][0] = "Foo"
# # print(id(l), l)
# # print(id(lc), lc)

# # print(l.count(1))
# # print(l.count(-11))
# # # l.extend(1)#TypeError: 'int' object is not iterable
# # print(l)
# # l.append([1,2,3,4])#TypeError: 'int' object is not iterable
# # l.extend([1,2,3,4])#TypeError: 'int' object is not iterable
# # print(l)
# # print(l.index(1))
# # print(l.index(1, l.index(1)+1))
# # # print(l.index(1, 8)) #ValueError: 1 is not in list
# # l.insert(3, "TEXT")
# # print(l)
# # l.insert(-3, "TEXT -3")
# # print(l)
# # l.insert(333, "TEXT 3333")
# # print(l)
# # e = l.pop()
# # print(e, l)
# # e = l.pop(5)
# # print(e, l)

# # e = l.remove(3.5)
# # print(e, l)
# # l.reverse()
# # print(l)
# # r = reversed(l)
# # print(f"{list(r)=}")
# # print(f"{l=}")
# # l.sort()#TypeError: '<' not supported between instances of 'str' and 'int'
# l = [21,3,214,23,5,436,32,5]
# print(l)
# l.sort()
# print(l)
# l = ["21","3","214","23","5","436","32","5"]
# print(l)
# l.sort()
# print(l)
# def f(element):
#     if type(element) in (int, float):
#         return element
#     elif type(element) in (str, list, tuple, set, dict):
#         return len(element)
#     elif element is None:
#         return 0
#     else:
#         return -1

# l = [1,2,"test", None, [1,2,3], 3.5]
# l.sort(key=f)
# print(l)
# print(all(l))
# print(all(l[1:]))
# print(any(l))
# print(list(enumerate(l)))
# print(len(l))
# # print(min(l))#TypeError: '<' not supported between instances of 'int' and 'NoneType'



l = [1,6,3,8,4,6,0,8]
print(l)
ls = sorted(l)
print(ls)
print(l)
l.sort()
print(l)
