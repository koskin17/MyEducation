class Quadrilateral:
    def __init__(self, width, height=0):
        self.width = width
        if height == 0:
            self.height = width
        else:
            self.height = height

    def __str__(self):
        if self.height == self.width:
            return f"Куб размером {self.width}x{self.height}"
        else:
            return f"Прямоугольник размером {self.width} x {self.height}"


q1 = Quadrilateral(10)
print(q1)
print(bool(q1))
q2 = Quadrilateral(3, 5)
print(q2)
print(q2 == True)
