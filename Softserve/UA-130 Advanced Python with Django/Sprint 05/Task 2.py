# Write  the function solve_quadric_equation(a, b, c) the three input parameters of which are numbers. The function should return 
# the solution of quadratic equation ax2+bx+c=0, where coefficients a, b, c are input parameters of  the function solve_quadric_equation:
#  in case of correct data the function should displayed the corresponding message – "The solution are x1=… and x2=…"
# in the case of division by zero the function should displayed the corresponding message – "Zero Division Error" 
# in the case of incorrect data the function should displayed the message – "Could not convert string to float"
# Note: in the function you must use the "try except" construct.  

#  Function example:
# solve_quadric_equation(1, 5, 6)            #output:   " The solution are x1=(-2-0j) and x2=(-3+0j)"
# solve_quadric_equation(0, 8, 1)            #output:   "Zero Division Error"
# solve_quadric_equation(1,”abc”, 5)       #output:   "Could not convert string to float"

# Вот решение задачи с использованием `try-except` для обработки ошибок:

import cmath

def solve_quadric_equation(a, b, c):
    try:
        # Check that a, b and c are numbers
        a, b, c = float(a), float(b), float(c)

        # Check for division by zero
        if a == 0:
            raise ZeroDivisionError

        # Calculating the discriminant
        D = b**2 - 4*a*c

        # Calculating roots of an equation using cmath (takes into account complex numbers)
        x1 = (-b - cmath.sqrt(D)) / (2 * a)
        x2 = (-b + cmath.sqrt(D)) / (2 * a)

        return f"The solution are x1={x1} and x2={x2}"

    except ValueError:
        return "Could not convert string to float"
    except ZeroDivisionError:
        return "Zero Division Error"

# Примеры вызова функции
solve_quadric_equation(1, 5, 6)       # Output: "The solution are x1=(-2-0j) and x2=(-3+0j)"
solve_quadric_equation(0, 8, 1)       # Output: "Zero Division Error"
solve_quadric_equation(1, "abc", 5)   # Output: "Could not convert string to float"

print(solve_quadric_equation(1, 3, -4))
print(solve_quadric_equation(1, 4, 5))
print(solve_quadric_equation(0, 5, 9))
print(solve_quadric_equation("a", 3, 1))

# ### **Объяснение кода**
# 1. **Преобразование `a`, `b`, `c` в `float`**:
#    - Если передано **не число**, возникает `ValueError`, и программа выводит `"Could not convert string to float"`.

# 2. **Проверка деления на ноль (`a == 0`)**:
#    - Если `a == 0`, квадратное уравнение **перестаёт быть квадратным**, и вызывается `ZeroDivisionError`.

# 3. **Расчёт корней**:
#    - Используем `cmath.sqrt(D)`, чтобы поддерживать **комплексные числа**.
#    - Вычисляем два корня `x1` и `x2`.
