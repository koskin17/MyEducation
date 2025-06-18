# Task2. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. 
# If the login is different, send an error message.
# (need to use loop while)

while True:
    log = str(input("Enter the login: "))
    if log == "First":
        print("Hello, First")
        break
    else:
        print("Something wrong.. Please, try again..")
