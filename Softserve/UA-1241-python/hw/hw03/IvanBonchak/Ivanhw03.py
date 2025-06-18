text = """ Beautiful is better than ugly. Explicit is better than implicit.
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
Namespaces are one honking great idea -- let's do more of those! """
# count the number "better", "never" та "is"
n_better = text.count("better")
n_never = text.count("never")
n_is = text.count("is")
print ("The count of 'better'-",n_better)
print("The count of 'never'-",n_never)
print("The count of 'is'-",n_is)
#text in upper case
print(text.upper())
#- replace all occurrences of the symbol “i” with “&”
print(text.replace("i","&"))
