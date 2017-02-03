from random_nums import random_nums

def shell_sort(nums):
    nums_len = len(nums)
    gap = nums_len // 2
    while gap > 0:
        for i in range(nums_len - gap):
            j = i
            key = nums[j+gap]
            while j >= 0 and key < nums[j]:
                nums[j+gap] = nums[j]
                j -= gap
            nums[j+gap] = key
        gap //= 2
    return nums

if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    shell_sort(nums)
    print(nums)
