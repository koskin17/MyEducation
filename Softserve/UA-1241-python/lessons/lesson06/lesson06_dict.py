# d = dict()
# print(type(d), d)
# d = dict([(1, 2), ("key", "value")])
# print(type(d), d)
# # d = dict([(1, 2), ("key", "value", 4)])#ValueError: dictionary update sequence element #1 has length 3; 2 is required

# d = {}
# print(type(d), d)
# d = {
#     1: 2, 
#     "key": "value"
# }
# print(type(d), d)
# print(d[1])
# print(d["key"])
# # print(d["key2"])#KeyError: 'key2'
# d[1] = "test"
# print(type(d), d)
# d["my_key"] = 3
# print(type(d), d)


# print([method for method in dir(dict) if not method.startswith("_")])
# print(d.get(1))
# print(d.get("foo"))
# print(d.get("foo", "null"))
# print(d.get("my_key", "null"))
# print(d.fromkeys("test", "muu"))
# print(d.items())
# print(d.keys())
# print(d.values())
# print(d.update({"tete": "te", "test2": 1516}))
# print(d)
# # print(d.pop())#TypeError: pop expected at least 1 argument, got 0
# print(d.pop("key"))
# print(d)
# d = {1: 'test', 'key': 'value', 'my_key': 3, 'tete': 'te', 'test2': 1516}
# for key in d:
#     print(key, d[key])

# for  key, value in d.items():
#     print(key, value)
i = int(input("number:"))
b = ""

while i >=2:
    print(i, end=" => ")
    b  += str(i%2)
    i = i//2
    print(f"{b=} {i=}")
b += str(i)
b = b[::-1]
print(b, int(b, 2))



