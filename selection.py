def selection(arr, size):
    for step in range(size):
        min_index = step
        for i in range(step + 1, size):
            if arr[i] < arr[min_index]:
                min_index = i
        (arr[step], arr[min_index]) = (arr[min_index], arr[step])

data = [2, 45, 23, 11, 9]
size = len(data)
selection(data, size)

print(data)


