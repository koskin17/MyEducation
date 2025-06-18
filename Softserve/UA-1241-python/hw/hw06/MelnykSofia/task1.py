range_list=list(range(1,11))
list_2=list()
list_3=list()
list_not_2_3=list()
for i in range(10):
    if range_list[i]%2==0:
        list_2.append(range_list[i])
    if range_list[i]%3==0 and range_list[i]%2>0:
        list_3.append(range_list[i])
    if range_list[i]%2 > 0 and range_list[i]%3 > 0:
        list_not_2_3.append(range_list[i])
# print(range_list)
print(f"Even numbers that are diisible by 2 {list_2}")
print(f"Odd numbers, which are divisible by 3 {list_3}")
print(f"Numbers that are notdivisible by 2 and 3 {list_not_2_3}")