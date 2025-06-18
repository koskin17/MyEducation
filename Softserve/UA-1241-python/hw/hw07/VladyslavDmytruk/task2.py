#Task2.
#Write a program that calculates the area of a rectangle, triangle and circle
#(write three functions to calculate the area. And call them in the main program 
#depending on the user's choice).

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    import math
    return math.pi * radius ** 2

def program():
    shape = input("Choose shape (rectangle/triangle/circle): ").lower()
    if shape == "rectangle":
        length = float(input("Length: "))
        width = float(input("Width: "))
        print(f"Area: {area_rectangle(length, width)}")
    elif shape == "triangle":
        base = float(input("Base: "))
        height = float(input("Height: "))
        print(f"Area: {area_triangle(base, height)}")
    elif shape == "circle":
        radius = float(input("Radius: "))
        print(f"Area: {area_circle(radius)}")
    else:
        print("Invalid choice!")

program()
