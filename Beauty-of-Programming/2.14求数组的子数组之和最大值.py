from random_nums import random_nums

def find_subarray_max(nums):
    s = nums[0]
    max_val = s
    for i in nums:
        s += i
        max_val = max(s, max_val)
        if s < 0:
            s = 0
    return max_val


if __name__ == "__main__":
    nums = random_nums(-10, 10, 10)
    print(nums)
    print(find_subarray_max(nums))
