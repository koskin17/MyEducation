# Task 1
container = list(range(1, 11))
for element in enumerate(container):
  index = int(element[0])
  container[index] = float(element[1])

print(container)


# Task 2
num = int(input("Enter a number: "))
i = 0
j = 1
while i <= num:
  print(i, end=" ")
  i, j = j, i + j


# Task 3
print()
num = int(input("Enter a number: "))
if num < 0:
  print("Factorial does not exist for negative numbers")
elif num == 0 or num == 1:
  print(1)
elif num == 2:
  print(2)
else:
  i = 1
  f = 1
  while i <= num:
    f = f * i
    i += 1
  print(f)
