#Task2. Write a script that checks the login that the user enters.
#If the login is "First", then greet the users. If the login is
#different, send an error message.
#(need to use loop while)

"""The first way"""

while True:
    login = input(" Enter your Login: ")
    if login == "First":
        print("Welcome!")
        break
    else:
     print("Error: Incorect login, try againe")
     break

"""The socond way"""

login = input("Enter your login: ")
while login:
    if login == "First":
        print("Welcome!")
        break
    else:
        print("Error: Incorect login, try again")
        break 