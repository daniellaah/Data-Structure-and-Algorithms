from random_nums import random_nums

def partition(nums, left, right):
    pivotIndex = left
    storeIndex = pivotIndex + 1
    for i in range(storeIndex, right):
        if nums[i] < nums[pivotIndex]:
            nums[i], nums[storeIndex] = nums[storeIndex], nums[i]
            storeIndex += 1
    nums[pivotIndex], nums[storeIndex-1] = nums[storeIndex-1], nums[pivotIndex]
    return storeIndex - 1

def quick_sort(nums, left, right):
    if right - left > 1:
        pivotIndex = partition(nums, left, right)
        quick_sort(nums, left, pivotIndex)
        quick_sort(nums, pivotIndex+1, right)

if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    quick_sort(nums, 0, len(nums))
    print(nums)
