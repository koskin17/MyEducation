from math import pi as pi_number, pow


def area_rectangle():
    sides_of_rectangle = input("Пожалуйста, укажите 2 стороны прямоугольника через запятую: ")
    if "," in sides_of_rectangle:
        sides_of_rectangle = sides_of_rectangle.replace(" ", "").split(",")
        if sides_of_rectangle[0].isdigit() and sides_of_rectangle[1].isdigit():
            sides_of_rectangle = list(map(int, sides_of_rectangle))
            print(f"Площадь прямоугольника со сторонами {sides_of_rectangle[0]} и {sides_of_rectangle[1]} равна:",
                  sides_of_rectangle[0] * sides_of_rectangle[1])
        else:
            print("Вы ввели не числа.")
    else:
        print("Пожалуйста, введите числа именно через запятую.")


def area_triangle():
    param_of_triangles = input("Пожалуйста, укажите длину основания треугольника и его высоту через запятую: ")
    if "," in param_of_triangles:
        param_of_triangles = param_of_triangles.replace(" ", "").split(",")
        if param_of_triangles[0].isdigit() and param_of_triangles[1].isdigit():
            param_of_triangles = list(map(int, param_of_triangles))
            print(f"Площадь треугольника с длинной основания {param_of_triangles[0]} и высотой {param_of_triangles[1]} "
                  f"равна: ", (param_of_triangles[0] * param_of_triangles[1] / 2))
        else:
            print("Вы ввели не числа.")
    else:
        print("Пожалуйста, введите числа именно через запятую.")


def area_circle():
    radius = input("Пожалуйста, укажите радиус круга для расчёта его площади: ")
    if radius.isdigit():
        print(f"Площадь круга с радиусом {radius} равна: ", pi_number * pow((int(radius), 2)))
    else:
        print("Вы ввели не числа.")
