# Модуль Simple Draw
from random import randint

import simple_draw as sd

# Если зажать Ctrl и мышкой на названии модуля, то откроется файл с содержанием этого модуля
# Находясь в этом файле можно в Pycharm нажать на структуру (левый нижний угол) и увидеть все переменные и функции,
# которые есть в этом модуле

sd.resolution = (1200, 600)
# 1. Нарисовать три вложенных окружности с шагом 5 пикселей
point = sd.get_point(100, 100)
radius = 50

for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)
    # Если стоять курсором внутри скобок и нажать Ctrl + P, то появится подсказка заполнения параметров для функции


# 2. Написать функцию рисования пузырька, принимающую 2 параметра: точка рисования и шаг
def bubble(start_point, step):
    bubble_radius = 50

    for _ in range(3):
        bubble_radius += step
        sd.circle(center_position=start_point, radius=bubble_radius, width=2)


point2 = sd.get_point(300, 300)
bubble(start_point=point2, step=10)

# 3. нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point3 = sd.get_point(x, 500)
    bubble(start_point=point3, step=5)

# 4. Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 300):
        point4 = sd.get_point(x, y)
        bubble(start_point=point4, step=5)

# 5. Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# sd.resolution = (1200, 600)
for _ in range(100):
    point5 = sd.random_point()
    step = randint(2, 10)
    bubble(start_point=point5, step=step)

sd.pause()
