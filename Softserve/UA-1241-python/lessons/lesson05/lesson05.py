# i = 1

# while i < 6:
#     print(i)
#     # i += 1
# # else:
# #     print("end while")

# print("end while")

# # while True:
# #     pass

# a = None
# b = None
# while not isinstance(a, int) and not isinstance(b, int):
#     a = input('a: ')
#     print(type(a), a)
    
#     b = input('b: ')
#     print(type(b), b)
#     if  a.isdigit() and b.isdigit():
#         a = int(a)
#         b = int(b)
#         print(f"{a/b =}")
#     else:
#         print("repit")


# for i in 15:#TypeError: 'int' object is not iterable
#     print()

# container = "abcdefgabcdefgabcdefg"
# unic = []

# for char in container:
#     print(char)
#     if char not in unic:
#         unic.append(char)

# print(f"{unic=}")
# container = [1,2,3,4,(1,2,3), "test"]
# for char in container:
#     print(char)

# r = range(10)
# print(r)
# print(list(r))
# r = list(range(-10))
# print(r)
# r = list(range(-10, 0))
# print(r)
# r = list(range(-3, 15))
# print(r)
# r = list(range(-3, 15, 3))
# print(r)
# # r = list(range(-3, 15, 3.5)) #TypeError: 'float' object cannot be interpreted as an integer

# container = [1,2,3,4,(1,2,3), "test"]
# for i in range(len(container)):
#     print(f"container[{i}]={container[i]}")


# for element in enumerate(container):
#     print(element, end=" => ")
#     print(f"container[{element[0]}]={element[1]}")


# a, b = 1, 2


# for index, value in enumerate(container):
#     print(f"container[{index}]={value}")


# matrix = [[1,2,3], "testdata", (1533, 58, 99)]

# for row in matrix:
#     for element in row:
#         print(element, end="\t")
#     print()

# l = list(range(20))
# print(l)
# sum = 0
# iter = 0
# for i in l:
#     print(f"{iter=}")
#     if i % 2:
#         sum += i
#         print(i, sum)
#         # if sum > 20:
#         #     break
#     iter += 1
# else:
#     print("end for")
    

# while True:
#     comand = int(input("input number:"))
#     if comand == 0:
#         break
#     print(f"command: {comand}")
# else:
#     print("end while")
# print("end program")


# while True:
#     print("enter exit for EXIT")
#     line = input("input number:")
#     if line.lower().strip() == "exit":
#         break
#     count = 0
#     for text in line.split():
#         print(text, end=" => ")
#         count += 1
#         if count > 5:
#             break
#     print()


# while True:
#     print("enter exit for EXIT")
#     line = input("input number:")
#     if line.lower().strip() == "exit":
#         break
#     sum = 0
#     for text in line.split():
#         print(f"{text} => ")
#         if not text.isdigit():
#             continue
#         sum += int(text)
#         print(f"\r\t{sum=}")        
#     print()

# for i in range(3):
#     pass #ToDo


# break #SyntaxError: 'break' outside loop


# for i in range(3):
#     temp = 25


# print(i)
# print(temp)

# for i in range(100):
#     if i % 2 == 0:
#         print(i, end=' ')
# print()
# for number in range(0, 100, 2):
#     print(number, end=" ")
# print()
# num = 0
# while num < 100:
#     if num % 2 == 0:
#         print(num, end=" ")
#     num += 1

# print()
# i = 0
# while i < 100:
#     if i % 2 != 0:
#         print(i, end=' ')
#     i += 1

# for num in range(100):
#     if num % 2 == 0:
#         continue
#     print(num, end=" ")

# from random import randint
# l = [randint(0, 100) for _ in range(100)]
# print(l)
# is_contain = False
# position = -1
# for i in range(len(l)):
#     if l[i] % 2:
#         is_contain = True
#         position = i
#         break

# print(f"contains odd number {is_contain} {position=}")

def числа(список):
    from random import randint
    random_list = [randint(0, 100) for _ in range(100)]
    print("random list:", random_list)
    for число in список:
        if число % 2 != 0:
            print("Список містить принаймні одне непарне число:", число)
            break
    else:
        print("Список не містить непарних чисел")

числа([2, 4, 6, 8, 10])
числа([2, 3, 6, 8, 10])