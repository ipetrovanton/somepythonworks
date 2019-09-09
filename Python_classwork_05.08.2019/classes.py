class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def place(self):
        if self.x == 0 and self.y == 0:
            return "Zero"
        elif self.x >= 0 and self.y >= 0:
            return "I"
        elif self.x <= 0 and self.y >= 0:
            return "II"
        elif self.x <= 0 and self.y >= 0:
            return "III"
        elif self.x <= 0 and self.y <= 0:
            return "IV"

    def len_to_zero(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


print(Coordinate(2, 4).place())
print(Coordinate(0, 0).place())
print(Coordinate(-1, 4).place())
print(Coordinate(-10, -9).place())
print(Coordinate(0, 4).place())
print(Coordinate(2, 0).place())
print(Coordinate(4, 3).len_to_zero())
