numb = range(1,11)
e_num =[]
o_num_3 = []
not_d2and3 =[]
for a in numb:
    if a % 2 ==0:
        e_num.append(a)
    elif a % 3 ==0:
        o_num_3.append(a)
    if a % 2 != 0 and a % 3 != 0:
        not_d2and3.append(a) 
print("even numbers that are divisible by 2", e_num)
print("odd numbers, which are divisible by 3", o_num_3)
print("numbers that are not divisible by 2 and 3", not_d2and3)