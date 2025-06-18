import math

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_circle(radius):
    return math.pi * radius * radius

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive number.")

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")

    if choice == 1:
        length = get_float_input("Enter the length of the rectangle: ")
        width = get_float_input("Enter the width of the rectangle: ")
        print(f"The area of the rectangle is {area_of_rectangle(length, width)}")
    elif choice == 2:
        base = get_float_input("Enter the base of the triangle: ")
        height = get_float_input("Enter the height of the triangle: ")
        print(f"The area of the triangle is {area_of_triangle(base, height)}")
    elif choice == 3:
        radius = get_float_input("Enter the radius of the circle: ")
        print(f"The area of the circle is {area_of_circle(radius)}")

if __name__ == "__main__":
    main()
