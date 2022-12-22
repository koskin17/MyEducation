'''
You are given a 2D array, composed of a colour and its 'common' association in each array element. The function you will write needs to return the colour as 'key' and association as its 'value'.

For example:
var array = [["white", "goodness"], ...] returns [{'white': 'goodness'}, ...]

'''

arr = [["white", "goodness"], ["blue", "tranquility"]]
def colour_association(arr):
    keys = []
    values = []
    new_list = []
    for i in range(len(arr)):
        keys.append(arr[i][0])
        values.append(arr[i][1])
    for i in range(len(keys)):
        tmp_dict = {keys[i]:values[i]}
        new_list.append(tmp_dict)
    return new_list

print(colour_association(arr))

''' Второй вариант '''
arr2 = [["white", "goodness"], ["blue", "tranquility"]]
def colour_association(arr2):
    return [{color: assoc} for color, assoc in arr2]
print(colour_association(arr2))
