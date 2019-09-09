user_Number = input("Введите пятизначное число: ")
try:
    number = int(user_Number)
except ValueError:
    print("Вы ввели не число")
try:
    if number % 100000 != number or number // 10000 < 1:
        raise Exception("Ваше число не пятизначное")
except Exception as e:
    exit(e)

for i in reversed(range(1, 6)):
    digit = (number % (10 ** i)) // (10 ** (i - 1))
    print("{} цифра равна {}".format(6-i, digit))


print("\nА теперь результат идентичный натуральному без страданий:\n")
for i in range(0, 5):
    print("{} цифра равна {}".format(i+1, user_Number[i]))