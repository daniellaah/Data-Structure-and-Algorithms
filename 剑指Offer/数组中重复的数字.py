from random import randint

'''面试题3（一）：找出数组中重复的数字
题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，
那么对应的输出是重复的数字2或者3。
'''
def duplicate1(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            tmp = nums[i]
            nums[i] = nums[tmp]
            nums[tmp] = tmp
    return None

'''面试题3（二）：不修改数组找出重复的数字
题目：在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至
少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的
数组。例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的
输出是重复的数字2或者3。
'''
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
