import random


def gen_password(num):
    password = ""
    for i in range(0, num):
        num = str(random.randrange(0, 10))
        big = str(chr(random.randrange(65, 91)))
        little = str(chr(random.randrange(97, 123)))
        sp = str(chr(random.randrange(58, 65)))
        sp1 = str(chr(random.randrange(91, 97)))
        list1 = [[big, little], [sp, sp1]]
        my_list = [list1[0][random.randrange(0, 2)], list1[1][random.randrange(0, 2)], num]
        password += str(my_list[random.randrange(0, 3)])
    return password


print(gen_password(10))
print(gen_password(8))
print(gen_password(20))
print(gen_password(33))
print(gen_password(4))
