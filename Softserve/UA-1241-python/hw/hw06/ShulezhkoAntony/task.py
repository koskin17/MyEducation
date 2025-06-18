#Task1
even = [x for x in range(1, 11) if x%2 == 0]
print(f'This numbers {even} are divisible by 2!')
odd = [x for x in range(1, 11) if x%3 == 0]
print(f'This numbers {odd} are divisible by 3!')
number = [x for x in range(1, 11) if x%2 == 1 and x%3 > 0]
print(f'You can`t divide this numbers {number} by 2 and 3!')

#Task2
while True:
  log = input('Write your login:')
  if log == 'First':
    print('Welcome!')
    break
  else:
    print("Error: Incorrect login. Please try again.")