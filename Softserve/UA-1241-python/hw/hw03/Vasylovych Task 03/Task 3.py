zen= """Beautiful is better than ugly.
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

#(find separately the number of occurrences of the words

print('Number of occurence of better:', zen.count('better'))
print('Number of occurence of never:', zen.count('never'))
print('Number of occurence of is:', zen.count('is'))


#def all latters in uppercase
print (zen.upper())


#def replace all occurrences of the symbol “i” with “&
replaced_text = zen.replace("i", "&")
print (replaced_text)

#product of number
n=1587
toList = [int(digit) for digit in str(n)]
print(sum(toList))

#reverse number
print(str(n)[::-1])

#Interchange the values of two variables without using the third variable.
a,b,c=78,34,90
c,b,a=a,b,c
print(a,b,c)






