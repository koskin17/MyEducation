def task_1(number_1, number_2):
    """function returns the largest number of two numbers"""
    return max(number_1, number_2)

def task_2(figure, *parameters):

    def area_rectangle(parameters): 
        return parameters[0]*parameters[1]
    
    def area_triangle(parameters):
        return parameters[0]*parameters[1]*0.5
    
    def area_circle(parameters):
        return round(parameters[0]**2 * 3.14159, 2)
    
    match figure:
        case "rectangle":
            return area_rectangle(parameters)
        case "triangle":
            return area_triangle(parameters)
        case "circle":
            return area_circle(parameters)
        case _:
            return f"{figure}: is not correct figure's name "
        

def task_3(word):
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else: result[letter] = 1
    return result
