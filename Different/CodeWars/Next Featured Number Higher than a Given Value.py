# Make a function that receives a value, val and outputs the smallest higher number than the given value,
# and this number belong to a set of positive integers that have the following properties:
#
# their digits occur only once
#
# they are odd
#
# they are multiple of three
#
# next_numb(12) == 15
#
# next_numb(13) == 15
#
# next_numb(99) == 105
#
# next_numb(999999) == 1023459
#
# next_number(9999999999) == "There is no possible number that fulfills those requirements"

def next_numb(val):
    for number in range(val+1, 9999999999+1):
        if number % 2 != 0 and number % 3 == 0:
            if all(str(number).count(letter) == 1 for letter in str(number)):
                return number

    return "There is no possible number that fulfills those requirements"




print(next_numb(12)) # 15
print(next_numb(13)) # 15
print(next_numb(99)) # 105
print(next_numb(999999)) # 1023459
print(next_numb(9999999999)) # "There is no possible number that fulfills those requirements")
