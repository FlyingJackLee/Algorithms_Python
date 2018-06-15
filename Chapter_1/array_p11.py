#1.1 Base Programming Model
#1.1 基础编程模型

def findMax(m):
    max = 0
    for value in m:
         if  max < value:
             max = value
    return max

def findAverage(m):
    sum = 0
    for value in m:
        sum += value
    return sum/len(m)

def makeCopy(m):
    copy = []
    for value in m:
        copy.append(value)
    #retrun m[:]
    return copy

def makeReverse(m):
    i =0
    N = len(m)
    while i < (N/2):
        temp = m[i]
        m[i] = m[N-1-i]
        m[N-1-i] = temp
        i += 1

def martrixMULT(a,b):
    i = j = k = temp = 0
    m = len(a)
    t = len(b)
    n = len(b[0])
    martrix = [[0 for t in range(m)] for t in range(n)]
    while i < m:
        while j < n:
            temp = 0
            while  k < t:
                temp += a[i][k] * b[k][j]
                k += 1
            martrix[i][j] = temp
            k = 0
            j += 1
        j = 0
        i += 1
    return martrix
