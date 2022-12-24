"""
A little coding task to practice detecting different types of item in a list,
and handling them appropriately. Given this list:
array = [102, 6.6, '77', '564', 75, '3.92', 'E', 2.77, 7.66, 'C', '408',
         605, '690', 'Z', '134', 'S', 'K', 148, '68', '654', 'U', '537',
         0.64, 905, 5.75, 302, '7.57', '834', '0.64', '29', '709', '8.28',
         'Y', 640, 'U', '0.92', 4.63, '259', '245', '5.1', 'Z', 'D',
         '5.58', 1.26, 6.95, '2.87', '9.25', 'F', 273, '852']
write a script to add up all the integers into one total, and all the float values into a second total,
but recognising that some integers and floats may be present in strings,
(e.g. in the last line '5.58' and 1.26 are both to be handled as floats,
and 273 and '852' both represent integer values).
Any strings that do not contain integers or floats are to be concatinated into a single string.
Print the total value of integers, the total value of floats, and the concatinated string.
"""
array = [102, 6.6, '77', '564', 75, '3.92', 'E', 2.77, 7.66, 'C', '408',
         605, '690', 'Z', '134', 'S', 'K', 148, '68', '654', 'U', '537',
         0.64, 905, 5.75, 302, '7.57', '834', '0.64', '29', '709', '8.28',
         'Y', 640, 'U', '0.92', 4.63, '259', '245', '5.1', 'Z', 'D',
         '5.58', 1.26, 6.95, '2.87', '9.25', 'F', 273, '852']

int_number = []
float_number = []
str_list = []
for item in array:
    if type(item) == int:
        int_number.append(item)
    elif type(item) == float:
        float_number.append(item)
    elif type(item) == str:
        if "." in item:
            float_number.append(float(item))
        else:
            try:
                int_number.append(int(item))
            except:
                str_list.append(item)

print(int_number)
print(float_number)
print(str_list)
