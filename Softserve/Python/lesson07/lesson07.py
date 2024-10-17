# def my_func():
#     print(">>>")
#     temp = 10
#     print(temp)
#     print("<<<")

# print(dir())
# print(my_func)
# print(type(my_func))
# my_func()
# my_func()
# my_func()
# my_func()
# help(print)
# print(print.__doc__)

# def greet(name):
#     """This function greets to
#     the person passed in as
#     parameter"""
#     print("Hello, " + name + ". Good morning!")

# help(greet)
# print(greet.__doc__)
# print(greet("Liubomyr"))
# greet("Anna")

# def is_positive(number):
#     if number >= 0:
#         return True
#     else:
#         return False
#     print("end func is_positive")
# value = is_positive(15)    
# print(value)
# print(is_positive(-22))

# def my_sum(a, b):
#     return f"{a}+{b}={a+b}"
# value =  my_sum(15, 22)
# print(type(value), value)


# def my_sum(a, b):
#     return f"{a}+{b}={a+b}", a+b
# value =  my_sum(15, 22)
# print(type(value), value)

# def reduse(l):
#     result = 0
#     for i in l:
#         result += i
#         print(f"{i} {result=}")
#         if result > 100:
#             return result
        
# print(reduse((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)))
# print(reduse((1,2,3,4,5,6,7,8,9)))


# def print_info(name):
#     print(">>> info <<<")
#     print(f"{name=}")
#     print("============")

# # print_info() #TypeError: print_info() missing 1 required positional argument: 'name'
# print_info("Olha")
# print_info("Olha", 20) #TypeError: print_info() takes 1 positional argument but 2 were given
        

# def print_info(name, age=18):
#     print(">>> info <<<")
#     print(f"{name=}")
#     print(f"{age=}")
#     print("============")
# # print_info() #TypeError: print_info() missing 1 required positional argument: 'name'
# print_info("Taras")
# print_info("Liubomyr", 38)

# def test(a, b=10, c): pass #SyntaxError: parameter without a default follows parameter with a default

# def print_info(name, age=18):
#     print(">>> info <<<")
#     print(f"{name=}")
#     print(f"{age=}")
#     print("============")

# # print_info("Liubomyr", 38)
# # print_info(38, "Liubomyr")
# print_info(age=38, name="Liubomyr")

# print(10, 25, 33, sep="=>")

# def func(a, b, *args, c=1, d=2, **kwargs):
#     print(f"{a=} {b=} {args=} {c=} {d=} {kwargs=}")

# func(1,2)
# func(1,2,3,4,5,6,7,8,9)
# func(1,2,3,4,5,6,7,8,9, c=88, k=15, g="test")

# def avr(*args):
#     # if len(args) == 0:
#     #     return 0 
#     # total_sum = sum(args)
#     # count = len(args)
#     # mean = total_sum / count
#     # return mean
    
#     # if len(args):     
#     #     total_sum = sum(args)
#     #     count = len(args)
#     #     mean = total_sum / count
#     #     return mean
#     # return 0

#     # if not len(args):     
#     #     return 0
#     # total_sum = sum(args)
#     # count = len(args)
#     # mean = total_sum / count
#     # return mean

#     args = [arg for arg in args if type(arg) in (int, float)]
#     if not len(args):     
#         return 0
#     total_sum = sum(args)
#     count = len(args)
#     mean = total_sum / count
#     return mean


# print(avr(1,2,3,7,8,9))
# print(avr(7,8,9))
# print(avr(7,8,9, "jsdhgk", []) )

# print(dir())
# g = "global"
# print(dir())

# def func():
#     print(dir())
#     print(g)
#     l = "local"
#     print(dir(), l)
# print(dir())
# func()
# func()

# print(l) #NameError: name 'l' is not defined



# g = "global"
# print(dir())

# def func():
#     print(dir())
#     print(g) #UnboundLocalError: cannot access local variable 'g' where it is not associated with a value
#     g = "l+g" 
#     l = "local"
#     print(dir(), l, g)

# func()
# print(g)


# g = ["global"]
# print(dir())

# def func():
#     print(dir())
#     print(g) 
#     g.append("l+g") 
#     l = "local"
#     print(dir(), l, g)

# func()
# print(g)


# g = "global"
# print(dir())

# def func():
#     global g
#     print(dir())
#     print(g) 
#     g = "l+g" 
#     l = "local"
#     print(dir(), l, g)

# func()
# print(g)
# local = "global"

# def f(text):
#     local = "local_1"

#     def inner():
#         nonlocal local
#         local = "local_2"
#         t = "local_inner"
#         print(">>> inner ",text, local)
#     inner()
#     print(">>> f ", local)

# f("test")
# print(">>>",local)


# def my_f(n):
#     for i in range(n):
#         print("\t"*i, i)
#     print("\t"*n, n)
#     for i in reversed(list(range(n))):
#         print("\t"*i, i)

# my_f(5)
# my_f(7)

# def my_f(n, current=0, up=True):
#     if current < 0:
#         return
#     print("\t"*current, current)
#     if current == n:
#         up=False
#     if up:
#         current += 1
#     else:
#         current -= 1
#     my_f(n, current , up)

    
# my_f(5, 3, False)
# my_f(4)



l = [1,2,3,4, "15", "test"]

def my_s(e):
    return e if type(e) in (int, float) else id(e)
l.sort(key=my_s)
print(l)
l.sort(key=lambda e: -e if type(e) in (int, float) else -id(e))
print(l)
print(dir())
f = lambda a, b: a**b
print(f(2,3))
print(f(2,3))
print(f(2,3))