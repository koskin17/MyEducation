list_1 = ['E_1','E_2','E_3','E_4','E_5','E_6','E_7','E_8']

partition_1 = list(zip(*[iter(list_1)] * 2))
partition_2 = list(zip(*[iter(list_1)] * 3))
partition_3 = list(zip(*[iter(list_1)] * 4))
partition_4 = list(zip(*[iter(list_1)] * 5))
partition_5 = list(zip(*[iter(list_1)] * 6))
partition_6 = list(zip(*[iter(list_1)] * 7))

print(partition_1)
print(partition_2)
print(partition_3)
print(partition_4)
print(partition_5)
print(partition_6)