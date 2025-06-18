# a = 5
# b = 6
# print(f"{a=} {b=} {a < b =}")
# print(f"{a=} {b=} {a > b =}")
# print(f"{a=} {b=} {a == b =}")
# print(f"{a=} {b=} {a != b =}")
# print(f"{a=} {b=} {a != b =}")

# a = "abc"
# b = "3s"
# print(f"{a=} {b=} {a < b =}")
# print(f"{a=} {b=} {a > b =}")
# print(f"{a=} {b=} {a == b =}")
# print(f"{a=} {b=} {a != b =}")
# print(f"{a=} {b=} {a != b =}")



# a = ("abc")
# b = 1
# print(f"{a=} {b=} {a < b =}")
# print(f"{a=} {b=} {a > b =}")
# print(f"{a=} {b=} {a == b =}")
# print(f"{a=} {b=} {a != b =}")
# print(f"{a=} {b=} {a != b =}")


# t = True
# f = False

# print(t and f)5


# a = float(input("a: "))
# print(a >= 0 and a <=10) #(0..10)
# print(a < 0 or a >10) # (..0, 10..)
# print(a < 0 or a >10 and a <20) # (..0, 10..20)



# print(12 and "test" and [1,2,3])

# is_false = [0, False, None, "", [], (), {}]

# print(12 and [] and 0 and "test" and [1,2,3])
# print(0 or [] or "" or {})
# print(0 or [] or "X" or {})


# a = [1]
# b = [1]
# c = a
# print(f"{a=} {id(a)=}")
# print(f"{b=} {id(b)=}")
# print(f"{c=} {id(c)=}")
# print(f"{a is b=}")
# print(f"{id(a) == id(b)=}")
# print(f"{a is c=}")
# print(f"{id(a) == id(c)=}")
# print(f"{a is not c=}")
# print(f"{id(a) != id(c)=}")
# print(f"{a==b}")


# 1 in 2.5 #TypeError: argument of type 'float' is not iterable


# l = [1, 2, 3, (9, 8), "test", [1, 2, "foo"]]

# print(f"{3 in l =}")
# print(f"{"test" in l =}")
# print(f"{"es" in l =}")
# print(f"{"foo" in l =}")
# print(f"{[1, 2, "foo"] in l =}")
# print(f"{"hoo" not in l =}")

# print(f"{"hoo"  in "text hoofoo" =}")
# print(f"{"hooh"  in "text hoofoo" =}")



# score = int(input("score: "))
# if score > 8:
#     print(">"*15)
#     print("You have passed the exam")
#     print("<"*15)

# print("Exam was finished.")


# temperature = float(input('What is the temperature? '))
# if temperature > 30:
#     print(">"*15)
#     print('Wear shorts.')
#     print("<"*15)
# else:
#     print("}"*15)
#     print('Wear long pants.')
#     print("{"*15)


# print('Get some exercise outside.')


# age = float(input('age: '))
# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')

# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')



# score = int(input("score: "))
# if score >= 90:
#     letter = 'A'
# else:
#     # grade must be B, C, D or F
#     if score >= 81:
#         letter = 'B'
#     else: # grade must be C, D or F
#         if score >= 71:
#             letter = 'C'
#         else: # grade must D or F
#             if score >= 61:
#                 letter = 'D'
#             else:
#                 if score >=51:
#                     letter = 'E'
#                 else:
#                     letter = 'F'

# if score >= 90:
#     letter = 'A'
# elif score >= 81:
#     letter = 'B'
# elif score >= 71:
#     letter = 'C'
# elif score >= 61:
#     letter = 'D'
# elif score >=51:
#     letter = 'E'
# else:
#     letter = 'F'

# print(f"my score {score} {letter}")

# is_student = True if score >= 51 else False
# print(is_student)

# is_student = "student" if score >= 51 else "not student"
# print(is_student)

# # is_student = score >= 51 ? "student" : "not student"

# is_student = None
# if score >= 51:
#     is_student = "student"
# else:
#     is_student = "not student"


# match score:
#     case 100|99|98|97|96|95|94|93|92|91:
#         letter = 'A'


# status = int(input("score: "))
# match status:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")

# match status:
#     case 400:
#         print("Bad request")
#     case 401|403 as error:
#         print(f'{error} is authentication error')
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")

values = input("comands: ").split()
print(values)
match values:
    case "load", link:
        print(f"load: {link}")
    case "save", link, filename:
        print(f"save: {link} >> {filename}")
    case "save", link, *filenames:
        print(f"save: {link} >> ")
        for filename in filenames:
           print(f"\t\t {filename}")
    case _:
        print(f"default(values)")