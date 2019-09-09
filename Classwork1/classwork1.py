def abs(number):
    if type(number) == int:
        return int((number**2)**0.5)
    else:
        return (number**2)**0.5

print("{}".format(abs(-5.6)))

def is_prime(a):
    for i in range(2, round(a / 2)):
        if not a % i:
            return False
    return True


for i in range(2, 1001):
    print("{} - {}".format(i, is_prime(i)))

def wave(s):
    length = len(s)
    newStrings = list()
    for i in range(0, length):
        arr_string = list(s)
        arr_string[i] = arr_string[i].upper()
        new_string = ''.join(arr_string)
        newStrings.append(new_string)
    print("{}".format(newStrings))


wave("hello!")
