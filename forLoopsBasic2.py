# 1.
def biggieSize(x):
    for i in range(len(x)):
        if x[i] > 0:
            x[i] = "big"
    print(x)

# y = [123,4,325,-1234,432,3,-5345,-1]
# biggieSize(y)

# 2.
def countPositives(x):
    count = 0
    for i in x:
        if i > 0:
            count += 1
    x[len(x) - 1] = count
    print(x)

# y = [123,4,325,-1234,432,3,-5345,-1]
# countPositives(y)

# 3. 
def sumTotal(x):
    sum = 0
    for i in x:
        sum += i
    print(sum)

# y = [123,4,325,-1234,432,3,-5345,-1]
# sumTotal(y)

# 4.
def average(x):
    sum = 0
    for i in x:
        sum += i
    ave = sum / len(x)
    print(ave)

# y = [123,4,325,-1234,432,3,-5345,-1]
# average(y)

# 5.
def length(x):
    print(len(x))

# y = [123,4,325,-1234,432,3,-5345,-1]
# z = []
# length(y)
# length(z)

# 6.
def minimun(x):
    if len(x) > 0:
        min = x[0]
        for i in x:
            if i < min:
                min = i
        print(min)
    else:
        print(False)

# y = [123,4,325,-1234,432,3,-5345,-1]
# minimun(y)
# z = []
# minimun(z)

# 7.
def maximusDecimusMeridius(x):
    if len(x) > 0:
        max = x[0]
        for i in x:
            if i > max:
                max = i
        print(max)
    else:
        print(False)
        
# y = [123,4,325,-1234,432,3,-5345,-1]
# z = []
# maximusDecimusMeridius(y)
# maximusDecimusMeridius(z)

# 8. 
def ultimateAnalysis(x):
    sum = 0
    min = x[0]
    max = x[0]
    for i in x:
        sum += i
        if i < min:
            min = i
        elif i > max:
            max = i
    ave = sum / len(x)

    newDict = {}
    newDict['sum'] = sum
    newDict['min'] = min
    newDict['max'] = max
    newDict['ave'] = ave
    newDict['len'] = len(x)
    print(newDict)

# y = [123,4,325,-1234,432,3,-5345,-1]
# ultimateAnalysis(y)

# 9.
def reverseList(x):
    for i in range(len(x)):
        if i <= (len(x) - 1) / 2:
            temp = x[i]
            x[i] = x[(len(x) - 1) - i]
            x[(len(x) - 1) - i] = temp
        else:
            break
    print(x)

# y = [123,4,325,-1234,432,3,-5345,-1]
# reverseList(y)



