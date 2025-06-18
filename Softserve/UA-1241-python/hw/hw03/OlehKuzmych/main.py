print("#1\n")


py_philosophy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

var1 = "better"
var2 = "never"
var3 = "is"

template = "In line \"{}\" found: " + var1 + " - {}, "+ var2 +" - {}, "+ var3 +" - {}"

for s in py_philosophy.splitlines():
    print( template
           .upper()
           .format( s.upper(), 
                    s.rstrip('.!,').split(' ').count(var1), 
                    s.rstrip('.!,').split(' ').count(var2), 
                    s.rstrip('.!,').split(' ').count(var3) ).replace("I","&") )


print("\n#2\n")

a = 129486573

result = 1
for n in str(a):
    result *= int(n)

print(result)
print(int(str(a)[::-1]))
print(int(''.join(sorted(str(a)))))


print("\n#3\n")

q = 5
w = 6
print(q, w)
q, w = w, q
print(q, w)
