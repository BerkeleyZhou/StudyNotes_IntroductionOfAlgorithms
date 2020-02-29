inNums = [2, 3, 2, 5, 1, 4, 7, 8, 6, 4]

def LinearSearch(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
    return None

print(LinearSearch(inNums, 10))