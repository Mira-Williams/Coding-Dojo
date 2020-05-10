
# 1.

def countdown(x):
    countdownList = []
    for i in range(x, -1, -1):
        countdownList.append(i)
    return countdownList

# print(countdown(24))

# 2.
def printAndReturn(x):
    print(x[0])
    return(x[1])

# y = [2,3]
# z = printAndReturn(y)
# print(z)

# 3.
def firstPlusLength(x):
    sum = x[0] + len(x)
    print(sum)

# y = [5,324,3246,54,7]
# firstPlusLength(y)

# 4.
def valGreaterThan2nd(x):
    newList = []
    count = 0
    if len(x) > 1:
        for i in x:
            if i > x[1]:
                newList.append(i)
                count += 1
        print(count)
        return(newList)
    else:
        return False

# y = [213,230,23,45,356,457,56,758]
# z = valGreaterThan2nd(y)
# print(z)

# a = [128]
# b = valGreaterThan2nd(a)
# print(b)

def lengthAndValue(x,y):
    newList = []
    for i in range(x):
        newList.append(y)
    print(newList)

# a = 22
# b = 11
# lengthAndValue(a,b)


    
