from random import randint

# 题目一
def duplicate1(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            tmp = nums[i]
            nums[i] = nums[tmp]
            nums[tmp] = tmp
    return None

# 题目二
def count_range(nums, start, end):
    count = 0
    for num in nums:
        if start <= num <= end:
            count += 1
    return count

def duplicate2(nums):
    n = len(nums)
    start = 1
    middle = n // 2
    end = n - 1
    while start < middle:
        if count_range(nums, start, middle) > (middle - start + 1):
            end = middle
            middle //= 2
        else:
            start = middle + 1
            middle = (start + end) // 2
    return start

if __name__ == '__main__':
    nums = [randint(1, 7) for _ in range(8)]
    print(nums)
    print(duplicate2(nums))
