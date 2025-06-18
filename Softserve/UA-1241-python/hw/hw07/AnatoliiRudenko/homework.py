import math
def largestnumber(a,b):
    """Returns largest number of two given numbers"""
    if a>b:
        print(a)
        return a
    elif b>a:
        print(b)
        return b
    else:
        print("Numbers are equal")
largestnumber(5,4)

def circle(r):
    print(math.pi*r*r)
    return math.pi*r*r
def rectangle(length, width):
    print(length*width)
    return length*width
def triange(base,height):
    print(1/2*base*height)
    return 1/2*base*height
i=input("Choose shape: ")
if i=="circle":
    radius=input("Enter radius: ")
    radius=int(radius)
    circle(radius)
elif i=="rectangle":
    length=input("Enter length: ")
    width=input("Enter width")
    length=int(length)
    width=int(width)
    rectangle(length, width)
elif i=="triangle":
    base=input("Enter base: ")
    height=input("Enter height: ")
    base=int(base)
    height=int(height)
else:
    print("Wrong shape")


def characters(text):
    dictionary={}
    for i in text:
        if i in dictionary:
            dictionary[i]=dictionary[i]+1
        else:
            dictionary[i]=1
    print(dictionary)

word=input("Enter word: ")

characters(word)