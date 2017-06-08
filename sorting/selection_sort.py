from random import randint
# time complexity: O(n^2)
# 循环遍历数组, 每次记录最大的数的索引, 与未排序的最后一个数交换
def selection_sort(nums):
    nums_len = len(nums)
    for i in range(nums_len - 1):
        max_idx = 0
        for j in range(1, nums_len - i):
            if nums[max_idx] < nums[j]:
                max_idx = j
        nums[max_idx], nums[j] = nums[j] , nums[max_idx]

if __name__ == "__main__":
    nums = [randint(0, 100) for _ in range(10)]
    print(nums)
    selection_sort(nums)
    print(nums)
