# 解法一: 快速排序
from random import randint

def partition(nums, pivot_idx):
    nums[pivot_idx], nums[0] = nums[pivot_idx], nums[0]
    pivot_idx = 0
    store_idx = pivot_idx + 1
    for i in range(store_idx, len(nums)):
        if nums[i] > nums[pivot_idx]:
            nums[i], nums[store_idx] = nums[store_idx], nums[i]
            store_idx += 1
    nums[pivot_idx], nums[store_idx-1] = nums[store_idx-1], nums[pivot_idx]
    return store_idx - 1

def find_k_big(nums, k):
    if k <= 0 or not nums:
        return []
    if k >= len(nums):
        return nums
    pivotIndex = partition(nums, randint(0, len(nums)-1))
    if k - 1 > pivotIndex:
        return nums[0: pivotIndex+1] + find_k_big(nums[pivotIndex+1:], k - (pivotIndex+1))
    elif k - 1 < pivotIndex:
        return find_k_big(nums[0: pivotIndex], k)
    else:
        return nums[0: k]

if __name__ == "__main__":
    nums = [randint(1, 20) for _ in range(20)]
    print(nums)
    print(find_k_big(nums, 4))
    #quick_sort(nums, 0, len(nums))
    #print(nums)
