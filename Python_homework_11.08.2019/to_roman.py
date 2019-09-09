# Напишите функцию to_roman, которая
# принимает целое число, а
# возвращает строку, отображающую
# это число римскими цифрами.Например, на
# вход подается 6, вернет "VI".Например, на
# вход подается
# 23, вернет "XXIII".Входные
# данные должны быть
# в диапазоне от 1 до 5000, если
# подается число не в этом
# диапазоне или не число, то
# должны выбрасываться ошибка
# типа NonValidInput. Этот
# тип ошибки вы
# должны создать
# сами.Также необходимо
# в папке с
# файлом, содержащей
# вашу функцию, создать
# файл tests.py, внутри
# которой необходимо определить тесты
# для вашей
# функции.Тесты должны
# покрывать все возможные
# поведения функции, включая
# порождения ошибки при плохих
# входных данных.

class NonValidInput(Exception):
    pass


def to_roman(number):
    if type(number) != int or number < 1 or number >= 5000:
        raise NonValidInput('Format of your number is incorrect!')

    roman_num = [['I', 'V'], ['X', 'L'], ['C', 'D'], 'M']
    num_list = []
    for i in str(number):
        num_list.append(i)
    num_list.reverse()
    arr = []
    step = 0
    while step != len(num_list):
        num = int(num_list[step])
        if num == 0:
            step += 1
            continue
        elif num == 4 and step != 3:
            n = roman_num[step][0] + roman_num[step][1]
            arr.append(n)
        elif num < 5:
            n = roman_num[step][0] * num
            arr.append(n)
        elif num == 9:
            n = roman_num[step][0] + roman_num[step + 1][0]
            arr.append(n)
        else:
            n = roman_num[step][1] + roman_num[step][0] * (num - 5)
            arr.append(n)
        step += 1
    arr.reverse()
    result = " ".join(arr)
    return result


print(to_roman(4999))
print(to_roman(505))
print(to_roman(347))
print(to_roman(10))
print(to_roman(999))
print(to_roman(4444))
print(to_roman(4470))

