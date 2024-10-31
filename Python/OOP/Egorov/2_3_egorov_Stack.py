class Stack:

    def __init__(self):
        self.values = []

    def push(self, element):
        """ Метод insert добавляет элемент в указанную позицию.
        Если указан 0, то элемент добавляется в начало списка"""
        self.values.insert(0, element)

    def pop(self):
        if len(self.values) == 0:
            print("Empty stack")
        else:
            return self.values.pop(0)

    def peek(self):
        if len(self.values) == 0:
            print("Empty stack")
        else:
            return self.values[0]

    def is_empty(self):
        if len(self.values) == 0:
            return True
        return False

    def size(self):
        return len(self.values)


s = Stack()
s.peek()
print(s.is_empty())
s.push("cat")
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(777)
print(s.pop())
print(s.pop())
print(s.size())
