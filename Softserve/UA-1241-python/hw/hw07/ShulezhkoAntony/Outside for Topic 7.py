#I. Jenny's secret message
def greet(name):
  if name == "Johnny":
    return "I love you, Johnny!"
  else:
    return (f"Hello, {name}!")

#II. Find The Distance Between Two Points
def calculate_distance(x1, y1, x2, y2):
  distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  return round(distance, 2)

#III. No yelling!
def filter(word):
  line = " ".join(word.split())
  return line[0].upper() + line[1:].lower()

#IV. Convert a Number to a String
def number_to_string(num):
  return string(num)

#V. Reversing Words in a String
def words_reverse(words):
  return (" ".join(words.split()[::-1]))

#VI. Reverse List Order
def list_reverse(list):
  return list[::-1]

#VII. Multiples of 3 or 5
def multiples(number):
  return sum([i for i in range(number) if i%3 == 0 or i%5==0])

#VIII. Will you make it?
def possible_or_not(dist_to_pump, mpg, fuel_left):
  return dist_to_pump - (mpg*fuel_left) <= 0

#IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
  return f"{name} plays banjo" if name[0].upper() == "R" else f"{name} does not play banjo"

#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_string(bool):
  return 'Yes!' if type == bool else 'No!'

#XI. Counting sheep
def count_sheep(sheep_list):
  return sheep_list.count(True)

#XII. Is this my tail?
def find_my_tail(body, tail):
    return body[-1] == tail