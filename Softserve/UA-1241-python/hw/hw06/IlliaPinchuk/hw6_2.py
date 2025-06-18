def check_login(valid_logins):
    valid_logins_set = set(valid_logins)
    while True:
        login = input("Enter login: ")
        if login in valid_logins_set:
            print("Welcome, user!")
            break
        else:
            print("Error: Invalid login. Please try again.")

valid_logins = {"First"}

check_login(valid_logins)
