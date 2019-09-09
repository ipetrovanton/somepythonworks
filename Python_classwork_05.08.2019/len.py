def func_len(a):
    count = 0
    for i in list(a):
        count += 1
    return count


print(func_len([1, 2, 3, 4]))


def func_revers(a):
    b = []
    for i in range(len(a) - 1, -1, -1):
        b.append(a[i])
    return b


print(func_revers([1, 2, 3, 4]))


def func_range(*params):
    arr = []
    if len(params) == 1:
        arr.append(params[0])
    elif len(params) == 2:
        l = params[1]
        arr.append(params[0])
        while l > 0:
            arr.append(arr[len(arr)-1] + 1)
            l -= 1
    elif len(params) == 3:
        l = params[1]
        arr.append(params[0])
        while l > 0:
            arr.append(arr[len(arr)-1] + params[2])
            l -= params[2]
    return arr


print(func_range(1))
print(func_range(0, 10))
print(func_range(0, 10, 2))
