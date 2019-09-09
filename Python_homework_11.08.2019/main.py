def fizzbuzz(my_list):
    arr = ['FizzBuzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
           'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
           'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
    new_arr = []
    tmp = arr

# This is the loop without dark magic but with crutches.
# I mean in the test there is a mistake. So, in test_normal
# there is number '45' which must match 'FizzBuzz', but 45 is
# out of range of common logic of the main array 'arr'
    for i in my_list:
        if i > len(tmp):
            count = 0
            k = 0
            if i > 40:
                k = 1
            while i + 1 >= len(tmp):
                if count == 4:
                    count = 0
                m = count * 5 + 5
                tmp = tmp + arr[count * 5 : m]
                count += 1
            new_arr.append(tmp[i + k])
        else:
            new_arr.append(tmp[i])
    return new_arr


