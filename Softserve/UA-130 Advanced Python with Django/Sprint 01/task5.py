# Convert a certain expression like 2+3 to expression in a postfix notation.

# The given expression can have one of the following tokens:

# a number;
# a parenthesis;
# arithmetic operator:
# subtraction (-);
# addition (+);
# multiplication (*);
# devision (/);
# modulo operation (%).
# Example:

# For expression = ["2","+","3"] the output should be ["2","3","+"].

# [execution time limit] 4 seconds (py)

# [input] array.string expression

# An array of tokes of a valid expression in the standard notation.

# [output] array.string

# Tokens of the expression in the postfix notation.
# Відповідь:(penalty regime: 0 %)

# Для преобразования инфиксного выражения в постфиксное (обратную польскую нотацию) можно использовать алгоритм сортировочной станции (Shunting Yard Algorithm), разработанный Э. Дейкстрой.
# Решение на Python
def toPostFixExpression(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}  # Приоритет операторов
    output = []  # Итоговый список (постфиксная нотация)
    operators = []  # Стек для операторов
    
    for token in expression:
        if token.isdigit():  # Число -> сразу в выходной список
            output.append(token)
        elif token in precedence:  # Оператор
            while (operators and operators[-1] != '(' and 
                   precedence[token] <= precedence.get(operators[-1], 0)):
                output.append(operators.pop())  # Переносим операторы с более высоким приоритетом
            operators.append(token)  # Добавляем текущий оператор в стек
        elif token == '(':
            operators.append(token)  # Открывающая скобка -> в стек
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())  # Переносим операторы до открывающей скобки
            operators.pop()  # Убираем '(' из стека
    
    while operators:
        output.append(operators.pop())  # Оставшиеся операторы в конец
    
    return output

# Пример использования
expression = ["2", "+", "3"]
print(toPostFixExpression(expression))  # Вывод: ['2', '3', '+']