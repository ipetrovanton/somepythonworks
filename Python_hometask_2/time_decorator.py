import time


def timeit(f):
    time_start = time.time()

    def wrap(*args):
        f(*args)
        print("Время выполнения функции {} seconds".format(time.time() - time_start))

    return wrap


@timeit
def factorialis(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print("Факториал числа {} равен {}".format(n, result))


factorialis(99999)
