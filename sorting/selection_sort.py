from random_nums import random_nums

def insertion_sort(nums):
    nums_len = len(nums)
    for i in range(nums_len):
        max_index = 0
        for j in range(nums_len - i):
            if nums[max_index] < nums[j]:
                max_index = j
        nums[max_index], nums[j] = nums[j], nums[max_index]
    return nums

if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    insertion_sort(nums)
    print(nums)
