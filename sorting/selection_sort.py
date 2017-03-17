from random_nums import random_nums

# time complexity: O(n^2)
def selection_sort(nums):
    nums_length = len(nums)
    for i in range(nums_length):
        max_idx = 0
        for j in range(nums_length - i):
            if nums[max_idx] < nums[j]:
                max_idx = j
        nums[max_idx], nums[j] = nums[j], nums[max_idx]
    return nums


if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    selection_sort(nums)
    print(nums)
