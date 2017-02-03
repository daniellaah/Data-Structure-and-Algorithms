from random_nums import random_nums
def bubble_sort(nums):
    nums_len = len(nums)
    for i in range(nums_len - 1):
        for j in range(nums_len - 1 -i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    bubble_sort(nums)
    print(nums)
