# Класс Деньги для работы с денежными суммами.
# Один объект должен быть иметь два аттрибута: рубли и копейки.
# Объект должен иметь метод, возращающий эквивалент объекта только в копейках в виде целого числа.
# На экран объект должен выводится как "x руб. y коп."
# (есть специальный магический метод, отвечающий за то, как объект выводится на экран).
# Реализовать сложение, вычитание и операции сравнения между объектами деньгами
# (для этого есть специальные магические методы).


class RussianMoney:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def getKop(self):
        return self.rub * 100 + self.kop

    def __repr__(self):
        return "{} руб. {} коп.".format(self.rub, self.kop)

    def __add__(self, other):
        summKop = self.getKop() + other.getKop()
        self.rub = summKop // 100
        self.kop = summKop % 100
        return self

    def __sub__(self, other):
        summKop = self.getKop() - other.getKop()
        self.rub = summKop // 100
        self.kop = summKop % 100
        return self

    def __eq__(self, other):
        return self.getKop() == other.getKop

    def __lt__(self, other):
        return self.getKop() < other.getKop()

    def __gt__(self, other):
        return self.getKop() > other.getKop()


myBudget = RussianMoney(100, 83)
price = RussianMoney(30, 54)

print(myBudget.getKop())
print(price.getKop())
print(myBudget - price)
if myBudget < price:
    print("Мало денег")
else:
    print("Денег достаточно - ты счастливый человек!")
if myBudget > price:
    print("Все нормально - супергуд!")
if myBudget == price:
    print("Тютелька в тютельку")

money = myBudget + price
print(money)
