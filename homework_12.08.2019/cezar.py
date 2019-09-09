# Cesar coder/decoder

class NonValidInput(Exception):
    pass


def code(s, key):
    if type(key) != int:
        raise NonValidInput('Format of your key is incorrect!')

    my_alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
                 "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" + \
                 "0123456789"
    a_list = list(my_alfabet)
    new_string = ""
    if key > 128:
        key = key % 128
    for i in s:
        if a_list.index(i) + key < len(a_list):
            new_string += a_list[a_list.index(i) + key]
        else:
            key -= 128
            new_string += a_list[(a_list.index(i) + key)]
    print(len(a_list))
    return new_string


print(code("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
           374583785782374828357848953748475378553384538839))


def de_code(s, key):
    if type(key) != int:
        raise NonValidInput('Format of your key is incorrect!')

    my_alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
                 "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" + \
                 "0123456789"
    a_list = list(my_alfabet)
    new_string = ""
    if key > 128:
        key = key % 128
    for i in s:
        if a_list.index(i) - key >= 0:
            new_string += a_list[a_list.index(i) - key]
        else:
            key -= 128
            new_string += a_list[(a_list.index(i) - key)]
    print(len(a_list))
    return new_string


print(de_code("ВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789abcdefghijkшщъыьэюяАБ",
              374583785782374828357848953748475378553384538839))
