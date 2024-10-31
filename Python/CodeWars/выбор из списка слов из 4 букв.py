x = ["Ryan", "Kieran", "Jason", "Yous"]

def friend(x):
    friend_name = []
    for name in x:
        if len(name) == 4:
            friend_name.append(name)
    return friend_name

print(friend(x))

''' Второй способ '''
def friend(x):
    return [f for f in x if len(f) == 4]
