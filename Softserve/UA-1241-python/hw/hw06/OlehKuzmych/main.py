#Task 1
for n in range(1, 11):
  if n % 2 == 0:
    print(f"{n} is even number that divisible by 2")

print("----------------")

for n in range(1, 11):
  if n % 2 != 0 and n % 3 == 0:
    print(f"{n} is odd number that divisible by 3")

print("----------------")

for n in range(1, 11):
  if n % 2 != 0 and n % 3 != 0:
    print(f"{n} is number that no divisible by 2 or 3")

#Task 2
while 1 == 1:
  login = str(input("Enter your login: "))
  if login == "First":
    break
  print("Wrong login")
