from random import randint
# time complexity: O(n^2)
# 循环遍历数组, 相邻两个比较, 交换顺序
def bubble_sort(nums):
    nums_len = len(nums)
    for i in range(1, nums_len):
        for j in range(nums_len - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

if __name__ == "__main__":
    nums = [randint(0, 100) for _ in range(10)]
    print(nums)
    bubble_sort(nums)
    print(nums)
