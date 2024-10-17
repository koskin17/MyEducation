# numbers = [0, 4, 3, 2, 3]
# doubled_numbers = []
# for n in numbers:
#     doubled_numbers.append(n * 2)

# print(doubled_numbers)

# doubled_numbers = [n**2 for n in doubled_numbers]
# print(doubled_numbers)


# doubled_odds = [n * 2 for n in range(10) if n % 2 == 1]
# print(doubled_odds)


# dodoubled_odds2 = []
# for n in range(10):
#      if n % 2 == 1:
#         dodoubled_odds2.append(n * 2)

# print(dodoubled_odds2)

# l1 = [1,2,3,4]
# l2 = ["a", "b", "c"]
# l3 = [97, 98, 99]
# pair = zip(l1, l2)
# print(pair)
# print(list(pair))
# pair3 = zip(l1, l2, l3)
# print(list(pair3))

# n = 3
# i = [r for r in range(n)]
# g = (r for r in range(n))
# print(f"{n=} i:{i.__sizeof__() } g:{g.__sizeof__()}")
# print(i)
# print(g)
# n = 330
# i = [r for r in range(n)]
# g = (r for r in range(n))
# print(f"{n=} i:{i.__sizeof__() } g:{g.__sizeof__()}")
# print(i)
# print(g)
# n = 3300
# i = [r for r in range(n)]
# g = (r for r in range(n))
# print(f"{n=} i:{i.__sizeof__() } g:{g.__sizeof__()}")
# # print(i)
# # print(g, list(g))


# line = input("data:")
# print(line)

# line.split()
# print(line.split())

# print(list(filter(lambda e: e.isdigit(), line.split())))
# print(list(map(int, (filter(lambda e: e.isdigit(), line.split())))))

# number = []
# def f(e):
#     return e.isdigit()

# l = line.split()
# print(l)
# ll = []
# for element in l:
#     if f(element):
#         ll.append(int(element))

# print(ll)

# print (['1', '2', '56', '446'])
# print(list(map(int, ['1', '2', '56', '446'])))
# t = []
# for i in ['1', '2', '56', '446']:
#     t.append(int(i))

# def a_add_b(a, b):
#     print(f"{a=} {b=} => {a+b}")
#     return a+b
# print(a_add_b(1,2))

# from functools import reduce

# print(reduce(a_add_b, [1,43,6,346,54,64,5]))
# print(reduce(a_add_b, [1,43,6,346,54,64,5], -19))

# l = [1 , 6, 5]
# s = "jbkfdgb"
# str
# r = range(15)
# print(l)
# print(s)
# print(r)
# for i in l:
#     i = i*10
#     print(i)
# print(l)
# it = iter(l)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# g = (i**i for i in [1,2,3])
# print(g)
# for i in g:
#     print(i)

# g = (i**i for i in [1,2,3])
# it = iter(g)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# class MyRange:
#     def __init__(self, start, stop=None, step=1):
#         if stop is None :
#             self.start = 0
#             self.stop = start
#         else:
#             self.start = start
#             self.stop = stop
#         self.step = step
#     def __str__(self):
#         return f"Range({self.start}, {self.stop}, {self.step})"
#     def __iter__(self):
#         print("__iter__")
#         self.current = self.start
#         return self
#     def __next__(self):
#         if self.current > self.stop:
#             raise StopIteration("my end")
#         value = self.current
#         self.current += self.step
#         return value

    
# r1 = MyRange(3)
# r2 = MyRange(-2, 3)
# r3 = MyRange(2,15,3)
# print(r1)
# print(r2)
# print(r3)

# for i in r1:
#     print(i)
# for i in r2:
#     print(i)
# for i in r3:
#     print(i)


# class MyList:
#     def __init__(self, *elements):
#        self.l = elements
#     def __str__(self):
#         s = ""
#         for e in self.l:
#             s += f"{str(e)},"
#         return f"<{s}>"

#     def __iter__(self):
#         print("__iter__")
#         self.current_index = 0
#         return self
#     def __next__(self):
#         if self.current_index >= len(self.l):
#             raise StopIteration("my end")
#         value = self.l[self.current_index]
#         self.current_index += 1
#         return value

    
# l = MyList(1,2,34,4,6,78)
# print(l)
# for i in l:
#     print(i)


# def my_gen():
#     yield 5
#     yield 6
#     yield 7
#     yield 8

# g = my_gen()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def my_gen(n):
#     print(f"my_gen start {n=}")
#     current = 0

#     print("while start")
#     while True:
#         print("while iter")
#         if current < n:
#             print(f"a:\t{current}")
#             yield current
#             print(f"b:\t{current}")
#             current += 1
#             print(f"c:\t{current}")
#         else:
#             break
# print(type(my_gen))
# # g = my_gen(5)
# # print(type(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))


# def star_decorator(funk):
#     print(f"funk {id(funk)}")
#     def inner(*args, **kwargs):
#         print("*"*5)
#         print(f"funk {id(funk)}")
#         funk(*args, **kwargs)
#         print("*"*5)
#     print(f"inner {id(inner)}")
#     return inner    



# @star_decorator
# def foo():
#     print( "foo")


# print(f"foo {id(foo)}")


# @star_decorator
# @star_decorator
# @star_decorator
# @star_decorator
# @star_decorator
# def boo():
#     print( "boo")

# print(f"boo {id(boo)}")
# foo()
# boo()

# def koo():
#     print("koo")

# koo = star_decorator(koo)
# koo = star_decorator(koo)
# koo = star_decorator(koo)
# koo = star_decorator(koo)
# koo = star_decorator(koo)

# # koo()

# def decorator(char, count=10):
#     print(f"run decorator {char=} {count=}")
#     def star_decorator(funk):
#         def inner(*args, **kwargs):
#             print(f"run {funk.__name__} {args=} {kwargs=}")
#             print(char*count)
#             result = funk(*args, **kwargs)
#             print(char*count)
#             return result
#         return inner    
#     return star_decorator


# # @decorator("+")
# # @decorator("=", 9)
# @decorator("*", 6)
# def my_funk( a, b, c, d=1, e=2):
#     print( f"{a=} {b=} {c=} {d} {e}")
# print("<>"*10)
# my_funk(1,2,3)
# # my_funk(1,2,3, d=22)

# import time

# def time_run(funk):
#     def inner(*args, **kwargs):
#         start = time.time()
#         result = funk(*args, **kwargs)
#         durattion =  time.time() - start
#         print(f"run {funk.__name__} {args=} {kwargs=} execution time={durattion}")
#         return result
#     return inner    

# @time_run
# def fibo1(n):
#     n1 = 1
#     n2 = 2
#     for _ in range(n):
#         n1, n2 = n2, n1+n2
#     return n1

# @time_run
# def fibo2(n):
#     if n < 1:
#         return 1
#     return fibo2(n-1) + fibo2(n-2)


# # print(fibo1(100))
# print(fibo2(10))

class A:
    def foo(self):
        print("A_ foo") 
    def boo(self):
        print("A_ boo") 

class B(A):
    def boo(self):
        print("B_ boo") 
    def old_boo(self):
        super().boo()

a = A()
a.foo()
a.boo()

b = B()
b.foo()
b.boo()
b.old_boo()
Exception
