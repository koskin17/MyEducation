def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"

def number_to_string(num):
    return str(num)

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

def count_sheeps(sheep):
    return sheep.count(True)

def distance(x1, y1, x2, y2):
    return round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 2)

def correct_tail(body, tail):
    return body[-1] == tail

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

def solution(number):
    return sum([i for i in range(number) if i%3 == 0 or i%5==0])

def filter_words(st):
    line = " ".join(st.split())
    return line[0].upper() + line[1:].lower()

def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]

def reverse(st):
    return " ".join(st.split()[::-1])

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump - (mpg*fuel_left) <= 0