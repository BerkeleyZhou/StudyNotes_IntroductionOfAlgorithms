import time

#Initial num list, none-ordered
inNums = [2, 3, 2, 5, 1, 4, 7, 8, 6, 4]


def InsertSort(nums):
    #i starts from 2 to the last element of the list
    for i in range(1, len(nums)):
        #store the key of teh value of the list in current index
        key = nums[i]
        j = i - 1
        #j starts from i-1 and become smaller each step
        while nums[j] > key and j >= 0:
            #move
            nums [j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

#test the time span of the algorithm
print(InsertSort(inNums))