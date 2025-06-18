num=7491
List = [int(digit) for digit in str(num)]
print(sum(List))
print(" ")

print(str(num)[::-1])
#start:stop:step. When you pass -1 as step, the start point goes to the end and stop at the front.
print(" ")

txt = '7491'
x = sorted(txt)
print(x)