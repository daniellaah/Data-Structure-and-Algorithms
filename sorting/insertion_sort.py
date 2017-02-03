from random_nums import random_nums

def insertion_sort(nums):
    nums_len = len(nums)
    for i in range(nums_len):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    insertion_sort(nums)
    print(nums)
