import time
import threading
import multiprocessing

print("Number of cpu : ", multiprocessing.cpu_count())


def timeit(f):
    def wrap(*args):
        time_start = time.time()
        print(f(*args))
        print("Время выполнения функции {} {} seconds\n".format((f), time.time() - time_start))

    return wrap


@timeit
def odd_primes(start, end):
    num_list = []
    flag = 0
    for i in range(start, end + 1):
        m = i
        if i > 4:
            m //= 2
        for k in range(2, m):
            if i % k == 0:
                flag += 1
                break
        if flag == 0:
            num_list.append(i)
        flag = 0
    return num_list


@timeit
def run_func0(odd_func):
    arr_nums = [[3, 5000], [5001, 10000], [10001, 20000]]
    for i in arr_nums:
        print(odd_primes(i[0], i[1]))

@timeit
def run_func(odd_func):
    threads = []
    arr_nums = [[3, 5000], [5001, 10000], [10001, 20000]]
    for i in arr_nums:
        thr = threading.Thread(target=odd_primes, args=(i[0], i[1]))
        threads.append(thr)
    for i in threads:
        i.start()
    for i in threads:
        i.join()


@timeit
def run_func1(odd_func):
    procs = []
    arr_nums = [[3, 5000], [5001, 10000], [10001, 20000]]
    for i in arr_nums:
        proc = multiprocessing.Process(target=odd_primes, args=(i[0], i[1]))
        procs.append(proc)
    for i in procs:
        i.start()
    for i in procs:
        i.join()


print("Один поток\n")
run_func0(odd_primes)
print("*********************************************"
      "*********************************************")
print("Разные потоки\n")

run_func(odd_primes)
print("*********************************************"
      "*********************************************")
print("\n Запуск функций c использованием multiprocessing.Process.\n")
run_func1(odd_primes)
