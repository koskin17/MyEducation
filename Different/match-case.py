"""
Конструкция позволяет избавиться от громоздких условий и цепочек if - else:
http_status = 400
if http_status == 400:
    print("Bad Request")
elif http_status == 403:
    print("Forbidden")
elif http_status == 404:
    print("Not Found")
else:
    print("Other")

Вместо можно использовать match-case:
http_status = 400
match http_status:
    case 400:
        print("Bad Request")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case _:
        print("Other")

"""
"Проверка дня недели """
from datetime import datetime

week = {0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"}

day = week.get(datetime.isoweekday(datetime.now()))
print(f"Сегодня {day}")
if day == "Sunday":
    print("Take it easy")
elif day == "Monday":
    print("Go to work")
elif day == "Tuesday":
    print("Work + Hobbies")
elif day == "Wednesday":
    print("Meetings")
elif day == "Thursday":
    print("Presentations")
elif day == "Friday":
    print("Interviews and party")
elif day == "Saturday":
    print("Time to do sports")
