# First

def count_numbers():
    res = {"divisible_by_2": 0, "divisible_by_3": 0, "not_divisible": 0}
    for x in range(1, 11):
        if x % 2 == 0:
            res["divisible_by_2"] += 1
        if x % 3 == 0:
            res["divisible_by_3"] += 1
        if x % 2 != 0 and x % 3 != 0:
            res["not_divisible"] += 1

    return res


# print(count_numbers())

# Task two

secret = "First"
users_password = input('Please enter the password: ')

while True:
    if users_password == secret:
        print("Welcome to the page")
        break
    else:
        users_password = input(
            'You have entered wrong password, please try again: ')
