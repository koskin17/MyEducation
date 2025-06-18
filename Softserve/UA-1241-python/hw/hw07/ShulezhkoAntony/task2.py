def area_rectangle(length, width):
  """
  Calculate the area of a rectangle.
  """
  return length * width
def area_triangle(base, height):
  """
  Calculate the area of a triangle.
  """
  return 0.5 * base * height
def area_circle(radius):
  """
  Calculate the area of a circle.
  """
  pi = 3.14159
  return pi * radius * radius
def main():
    print("Choose the shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter the number of your choice (1/2/3): ")

    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")

    elif choice == "2":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_triangle(base, height)
        print(f"The area of the triangle is: {area}")

    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        area = area_circle(radius)
        print(f"The area of the circle is: {area}")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()