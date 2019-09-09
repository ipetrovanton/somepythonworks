arr = [0, 3, 24, 2, 3, 7]
for i in range(0, len(arr)):
    minNum = arr[i]
    for k in range(i, len(arr)):
        if arr[k] < minNum:
            minNum = arr[k]
            tmp = arr[i]
            arr[i] = arr[k]
            arr[k] = tmp
print(arr)