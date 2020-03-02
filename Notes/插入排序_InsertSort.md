# 2.1插入排序的基本问题描述

输入一个数组，然后按照从小到大的顺序排列数组

## 插入排序伪代码

![image-20200222164202149](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200222164202149.png)

这里i是从j-1向前循环，如果A[i]还是比key值大，就把它往后移动一格

## 算法的可视化示意图

![image-20200222164122790](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200222164122790.png)

## 循环不变式

循环不变式的定义：

**初始化**：保证循环不变式在第一轮循环开始前是正确的

**保持**：如果每一次循环迭代是正确的，那么下一轮迭代也必定是正确的

**终止**：当循环结束后，不变式给我们得出一个有用的结论，证明算法的正确性

## 插入排序中的循环不变式

![image-20200222164301561](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200222164301561.png)

## 线性查找练习

![image-20200222164338777](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200222164338777.png)

**伪代码**

```
LINEAR-SEARCH(A, v)
    for i = 1 to A.length
       if A[i] == v
            return i
    return NIL
```

**循环不变式分析**

**初始化**：i等于1的时候，我们已经检查的元素组成的列表是一个空表

**保持**：每一步计算，我们都可以确定子列表A[1...i-1]是已经检查过的列表，即A[1...i-1]中没有和v相等的元素了。这个时候，我们比较v和A[i]如果他们相等，那我们就可以返回这个正确的答案，否则，我们就进入下一个循环

**结束**：结束时i等于A.Length+1，这个时候A[i...A.Length]中都没有和v相等的元素，即返回NIL

# 2.2 算法分析

**概念 输入规模**：对于许多问题来说最自然的输入规模度量就是输入的元素个数，例如待排序数组的大小n。当然，对于另一些问题，输入规模的最好度量方法是输入数据在二进制下的表示位数。还有时候，输入规模用两个数来表示更好

**概念 运行时间**：特定输入规模下，所执行的基本步骤数。首先，每次执行一行代码都需要话一定时间，虽然每一行所花的时间可能时不一样的，但是我们都假定每次执行i行耗时ci

## 插入排序的算法分析

```
1	INSERTION-SORT(A)									cost		times
2		for j <- 2 to length[A]							c1			n
3			do key <- A[i]								c2			n-1
4			//Insert A[j] into the sorted array			0			n-1
5			i <- j-1									c4			n-1
6			while i > 0 and A[i] > key					c5			sum(j=2,n,tj)
7				do A[i+1] <- A[i]						c6			sum(j=2,n,tj-1)
8				i <- i-1								c7			sum(j=2,n,tj-1)
9			A[i+1] <- key								c8			n-1
```

经过分析我们可以得知

算法的总运行时间是

![image-20200229112715179](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200229112715179.png)

插入排序算法在最优情况下和最差情况下的运行时间也是不同的

当输入数组按照顺序排列，对于第五行的while循环

每次取到的初始值A[i]都必然小于key值

那么while循环直接结束到达第9行

此时的最佳运行时间为

![image-20200229112752269](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200229112752269.png)

但是，如果输入的数组是倒序排列

第六行执行的次数为n!-1，第七行和第八行执行的次数为(n-1)!

![image-20200229113114172](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200229113114172.png)

那么这一最坏情况可以表示为

![image-20200229113158890](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200229113158890.png)

## 增长量级

在对插入排序的分析中，我们抽象化了每一个语句耗费的单位时间，现在，继续抽象化最坏情况的耗时表达式

即运行时间的rate of growth或者order of growth

插入排序的最坏时间代价为theta(n^2)

通常，如果一个算法的最坏运行时间代价要比另一个算法的最坏运行时间代价要低，我们就认为这个算法效率更高

Eg.在输入规模足够大的情况下，theta(n^3)的算法总比theta(n^2)的算法耗时高



# 2.3 算法的设计

插入排序的算法设计逻辑是增量的方法：在拍好序列的子数组种插入未排序的元素

还有一种设计策略叫做分治法

## 分治法

分治法的主要思想是把一个大问题分解成n个规模较小而结构与原问题相似的子问题；递归的解决这些问题最后再合并结果

所以分治在每一层递归上都有以下步骤

分解：将原问题分解成一系列子问题

解决：递归地解决子问题，如果问题地规模已经足够小，那么直接求解

合并：将子问题地结果合并成为原问题地解

在合并排序（Merge Sort）中，操作如下

![image-20200302144620406](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200302144620406.png)

在对子序列进行排序地时候，当序列长度为1的时候可以认为序列已经是排列完成的

Merge Sort中核心的方法是Merge方法MERGE(A, p, q, r)

这个方法A是序列，pqr都是角标。它的操作是假设A[p...q]和A[q+1...r]都是已经排好的有序数列，merge函数将会把这两个子数列合并，得到一个A[p,r]排列好的有序数列

![image-20200302145652072](C:\Users\Berke\AppData\Roaming\Typora\typora-user-images\image-20200302145652072.png)

## 在Python中实现Merge函数

```python
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
```

