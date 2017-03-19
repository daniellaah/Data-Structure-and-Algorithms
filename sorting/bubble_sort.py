from random_nums import random_nums
# time complexity: O(n^2)
# 循环遍历数组, 相邻两个比较, 交换顺序
def bubble_sort(nuns):
    nums_length = len(nums)
    for i in range(nums_length - 1):
        for j in range(nums_length - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    bubble_sort(nums)
    print(nums)
