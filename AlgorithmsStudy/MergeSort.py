def Merge(A, p, q, r):
    #左列表长度
    n1 = q - p + 1
    #右列表长度
    n2 = r - q
    #左列表
    L = A[p:q+1]
    #右列表
    R = A[q+1:]

    #初始化左右列表的指针
    i = 0
    j = 0

    #循环整个数组
    for k in range(p,r):
        #左列表已经空了
        if (i >= n1 and j < n2):
            A[k] = R[j]
            j += 1
        #右列表已经空了
        elif (i < n1 and j >= n2):
            A[k] = L[i]
            i += 1
        #都还有，可以比较
        else:
            if (L[i] <= R[j]):
                A[k] = L[i]
                i += 1
            elif (L[i] > R[j]):
                A[k] = R[j]
                j += 1

    return A

testList = [1,3,5,7,8,9,2,3,4,7,8]
retList = Merge(testList, 0, 5, 10)
print(retList)