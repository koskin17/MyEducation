"""Представьте, что в вашей машине есть встроенный тайм-трекер,
который отсчитывает длительность вашей поездки в минутах.
На старте на нем стоит время 00:00.

Напишите функцию, которая будет принимать длительность поездки в минутах (n)
и высчитывать время окончания поездки. Возвращать функция должна сумму цифр,
которые будут высвечиваться на тайм-трекере на финише при заданной длительности поездки."""

def timetracker(n):
    hour = n // 60
    minutes = n % 60

    hour = str(hour) if len(str(hour)) == 2 else "0" + str(hour)
    minutes = str(minutes) if len(str(minutes)) == 2 else "0" + str(minutes)

    return hour + ":" + minutes

time_driving = input("Укажите длительность поездки в минутах: ")
print(timetracker(int(time_driving)))

# Вариант 4
# def car_timer(n):
#     return sum(map(int, str(n // 60) + str(n % 60)))
#
# Вариант 5def car_timer(n):
#     h, m = divmod(n, 60)
#     H = str(h).zfill(2)
#     M = str(m).zfill(2)
#     return sum(int(x) for x in H) + sum(int(y) for y in M)

# Вариант 2
# def time_track(count_minutes: int):
#     return f'{count_minutes // 60:0>2}:{count_minutes % 60:0>2}'
#
# print(time_track(62))  # 01:02
#
# Вариант 3
# def time (x):
#     return  (x // 60 + (x % 60)*0.01)


