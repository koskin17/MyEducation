# First task
python_values = """
    Beautiful is better than ugly.
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
    Namespaces are one honking great idea -- let's do more of those!
"""
better = "better"
never = "never"
var_is = "is"

print(f"World {better} is mentioned {python_values.count(better)} times")
print(f"World {never} is mentioned {python_values.count(never)} times")
print(f"World {var_is} is mentioned {python_values.count(var_is)} times")
print(python_values.upper())
print(python_values.replace("i", "&").replace("I", "&"))

# Second task
class CalculatingFromNumber:
    def __init__(self, initial_value):
        self.initial_value = initial_value
    
    def sum(self):
        transform_value = str(self.initial_value)
        res = 0
        for num in transform_value:
            res += int(num)
        print(res)
        return res
    
    def reverce(self):
        transform_value = int(str(self.initial_value)[::-1])
        print(transform_value)
        return transform_value
    
    def order_by_acs(self):
        transform_value = sorted(str(self.initial_value))
        res = int(''.join(transform_value))
        print(res)
        return res

calculate = CalculatingFromNumber(7431)
calculate.order_by_acs()
calculate.sum()
calculate.reverce()


# Third task
var_1 = "Hello"
var_2 = "Summer"
var_1, var_2 = var_2, var_1
print(var_1)
print(var_2)




