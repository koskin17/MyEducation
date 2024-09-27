import json

file_cars = open("cars.json", "r")
file_cars2 = open("cars2.json", "r")
result_file = open("result.json", "w")

cars = json.load(file_cars)
cars2 = json.load(file_cars2)

cars.append(cars2)

file_cars.close()
file_cars2.close()

cars_sorted = sorted(cars, key=lambda x: x['max_speed'])

with open(r"result.json", 'w') as result_file:
    json.dump(cars_sorted, result_file)