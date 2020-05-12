def selectSort(x):
    start = 0
    while start < len(x):
        min = x[start]
        for i in range(start, len(x)):
            if x[i] < min:
                min = x[i]
                min_index = i
        temp = x[start]      
        x[start] = min
        x[min_index] = temp
        start += 1
    print(x)

y = [213,1234,34,5,3456,4,7,546,231,21,3,345,654]
selectSort(y)
