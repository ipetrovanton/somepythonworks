# Написать класс  Rectangle, который имеет длину и ширину и методы вычисления периметра и площади.
# Создайте класс Square. Он должен иметь такие же методы, что и прямоугольник
# Подумайте над тем, можно ли применить наследование при создании двух этих классов


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(length=self.side, width=self.side)


rectangle = Rectangle(10, 20)
print(rectangle.perimeter())
print(rectangle.square())

square = Square(10)
print(square.perimeter())
print(square.square())
