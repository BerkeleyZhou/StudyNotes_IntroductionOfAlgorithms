#Initial num list, none-ordered
inNums = [2, 3, 2, 5, 1, 4, 7, 8, 6, 4]

def InsertSortNoneIncrease(nums):
    #i starts from second last element and minus 1 each step
    for i in range(len(nums)-2, -1, -1):
        key = nums[i]
        j = i + 1
        while j < len(nums) and nums[j] > key:
            nums[j - 1] = nums[j]
            j += 1
        nums[j - 1] = key
    return  nums

print(InsertSortNoneIncrease(inNums))