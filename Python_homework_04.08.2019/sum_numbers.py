# Напишите
# функцию, которая определяет
# сумму цифр переданного
# ей числа (например, входные
# данные - число 126, выходные - число
# 9, так как 1 + 2 + 6 равно 9)

def sum_of_numbers(number):
    s = list(str(number))
    my_sum = 0
    for i in s:
        my_sum += int(i)
    return my_sum


# напишите функцию count_words(),
# которая принимает список строк и
# возвращает int число уникальных слов в этом списке
def count_words(s):
    my_dict = {}
    for i in s:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return len(my_dict)


list_of_strings = ['hello', 'hi', 'hello', 'goodbye', 'chao', 'hi']
print(count_words(list_of_strings))
