def to_title(s):
    a = s.split(" ")
    arr = []
    for i in a:
        arr.append(i.capitalize())
    new_s = " ".join(arr)
    return new_s


print(to_title("строка со словами с большой буквы"))


def symbol_counter(string, symbol):
    count = 0
    arr = list(string)
    for i in arr:
        if i == symbol:
            count += 1
    return count


print(symbol_counter("йцукенйцукен Йцукен некуЙ некуй", 'й'))


def my_print(*args):
    s = args[0]
    arr = str(s).split(" ")
    for i in range(0, len(arr)):
        n = 1
        if '{}' in arr[i]:
            arr[i] = args[n]
            n += 1
    my_str = " ".join(arr)
    print(my_str)
    return my_str


my_print('Coordinates: {}, {}', '37.4N', '-118.3W')
