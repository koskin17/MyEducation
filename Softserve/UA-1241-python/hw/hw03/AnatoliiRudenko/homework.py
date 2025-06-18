python_philosophy="""Beautiful is better than ugly.
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

word1="better"
word2="never"
word3="is"

print(python_philosophy.count(word1))
print(python_philosophy.count(word2))
print(python_philosophy.count(word3))

print(python_philosophy.upper())
print(python_philosophy.replace("i", "&"))


number=input("Enter number: ")
sum1=int(number[0])+int(number[1])+int(number[2])+int(number[3])
print(int(number[0])+int(number[1])+int(number[2])+int(number[3]))

reverseorder=int(number[3])+int(number[2])+int(number[1])+int(number[0])
print(number[3]+number[2]+number[1]+number[0])

print(sorted(number))


a=1
b=2
a,b=b,a
print(a,b)