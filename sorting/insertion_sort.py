from random_nums import random_nums
# time complexity: O(n^2)
# 首先将第一个数看成已经排好的数组, 将第二个数按照顺序插入到这个数组中, 以此类推
def insertion_sort(nums):
    nums_length = len(nums)
    for i in range(1, nums_length):
        current = nums[i]
        j = i - 1
        while j >= 0 and current < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current
    return nums

if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    insertion_sort(nums)
    print(nums)
