def get_lucky(my_list):
    res = []
    for el in my_list:
        if '7' in str(el):
            res.append(el)
    return res


# a = 3
# b = 5
# c = a * b
# first_list = [56, 78, 123, 7, 0]
# result = get_lucky(first_list)
# print(result)
