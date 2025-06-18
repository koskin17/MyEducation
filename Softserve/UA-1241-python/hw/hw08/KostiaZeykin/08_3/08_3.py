from calc_module import *

user_input = input("Укажите, пожалуйста, площадь какой фигуры Вы хотите посчитать (1 - прямоугольника, "
                   "2 - треугольника, 3 - круга): ")

if user_input.isdigit() and int(user_input) in (1, 2, 3):
    if int(user_input) == 1:
        area_rectangle()
    elif int(user_input) == 2:
        area_triangle()
    else:
        area_circle()
else:
    print("Пожалуйста, сделайте выбор из указанных вариантов.")
