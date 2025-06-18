correct_login = "First"
user_login = ""

while user_login != correct_login:
    user_login = input("Enter your login: ")
    if user_login == correct_login:
        print("Hello, Muchacho!")
    else:
        print("Error: Invalid login. Please try again.")
