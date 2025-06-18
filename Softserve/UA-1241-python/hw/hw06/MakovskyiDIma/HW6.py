numbers = list(range(1, 11))

def get_numbers_who_divisible_by_2(numbers):
    return [i for i in numbers if i%2 == 0]

def get_numbers_who_divisible_by_3_and_odd(numbers):
    return [i for i in numbers if i%2 == 1 and i%3 == 0]

def get_numbers_who_not_divisible_by_2_and_3(numbers):
    return [i for i in numbers if i%2 == 1 and i%3 > 0]

print(get_numbers_who_divisible_by_2(numbers=numbers))
print(get_numbers_who_divisible_by_3_and_odd(numbers=numbers))
print(get_numbers_who_not_divisible_by_2_and_3(numbers=numbers))

#___________________________________________________________________________________

while True:
    login = input("Write your login: ")
    if login == "First":
        print(f"Hellow {login}")
        break
    print("Error: invalid login")