"""Task 1"""


def largest_number(lst):
    """This function returns the largest number of two receiving from user"""
    lst.sort()
    print(lst)
    return print(f"Наибольшее из введённых чисел: {lst[1]}")


user_input = input("Пожалуйста, введите два числа через запятую: ")
if "," in user_input:
    user_input = user_input.replace(" ", "").split(",")
    if user_input[0].isdigit() and user_input[1].isdigit():
        user_input = list(map(int, user_input))
        largest_number(user_input)
    else:
        print("Вы ввели не числа.")
else:
    print("Пожалуйста, введите числа именно через запятую.")

"""Task 2"""


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
        print(f"Площадь круга с радиусом {radius} равна: ", 3.14 * (int(radius)**2))
    else:
        print("Вы ввели не числа.")


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

"""Task 3"""


def count_letter(user_input):
    for letter in user_input:
        if letter != " ":
            number_characters[letter] = user_input.count(letter)
        else:
            continue

    return print(number_characters)


number_characters = {}
user_string = input("Пожалуйста, введите любую строку: ").lower()
count_letter(user_string)
