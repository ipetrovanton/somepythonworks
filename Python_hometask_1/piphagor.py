import math

print("Введите длину катета 'a'")
a = float(input())
print("Введите длину катета 'b'")
b = float(input())

hipotenusa = (a*a + b*b) ** 0.5
print("Гиппотенуза равна: {}".format(hipotenusa))
