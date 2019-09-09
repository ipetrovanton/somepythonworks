from itertools import chain, filterfalse
# Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]),
# а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])


# метод chain склеивает несколько массивов в один
def to_one_list(*args):
    my_list = []
    for i in args:
        my_list = list(chain(my_list, i))
        print(my_list)
    return my_list


print("{}".format(to_one_list([1, 2], [3, 4], [5, 6])))

# Функция принимает массив (['hello', 'i', 'write', 'cool', 'code'])
# и возвращать массив из элементов,
# у которых длина не меньше пяти (['hello', 'world'])


def word_chooser(arr, l):
    new_arr = list(filterfalse(lambda x: len(x) < l, arr))
    return new_arr
# метод filterfalse отбирает значение, если условие false
# метод работает на черной магии лямбда функций, иначе его
# использование видится нецелесообразным ввиду необходимости создания
# еще функций, что раздувает код

print(f"{word_chooser(['hello', 'i', 'write', 'cool', 'code'], 5)}")
