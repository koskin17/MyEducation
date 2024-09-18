import json
import pprint

x = '{ "name":"Liubov", "age":25, "city":"Lviv"}'  # some JSON
y = json.loads(x)  # parse
print(y)
print(y["name"])


with open("lessons\lesson14\menu.json") as file:
    menu = json.load(file)  # parse
pprint.pprint(menu)


x = {"name": "Liubov", "age": 25, "city": " Lviv"}
json_format = json.dumps(x)
print(type(json_format), json_format)


with open(r"lessons\lesson14\user.json", "w", ) as file:
    json.dump(x,  file)  # parse

