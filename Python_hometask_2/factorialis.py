def factorialis (n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    print("Факториал числа {} равен {}". format(n, result))

factorialis(5)
