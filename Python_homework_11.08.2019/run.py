def getlucky(a):
    new_arr = []
    for i in list(a):
        count = 0
        for k in str(i):
            if k == '7':
                count += 1
        if count != 0:
            new_arr.append(i)
    return new_arr


print(getlucky([1210293819, 777, 82734982, 23432, 190312341123, 7]))


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise Exception("Radius less than Zero!")
        self.radius = radius
        self.diameter = self.radius * 2

    def area(self):
        return self.radius * 2 * 3.14 * 3.14

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius


okr = Circle(5)
okr7 = Circle(5)
okr2 = Circle(6)
print(okr == okr2)
print(okr != okr2)
print(okr == okr7)
print(okr != okr7)
print(okr == okr2)
print(okr != okr2)
print(okr.area())


def get_lucky(my_list):
    res = []
    for el in my_list:
        if '7' in str(el):
            res.append(el)
    return res


a = 3
b = 5
c = a * b
first_list = [56, 78, 123, 7, 0]
result = get_lucky(first_list)
print(result)
