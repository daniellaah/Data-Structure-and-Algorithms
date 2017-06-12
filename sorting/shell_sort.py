from random import randint
# 先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
# 待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
# def shell_sort(nums):
#     nums_len = len(nums)
#     gap = nums_len // 2
#     while gap > 0:
#         for i in range(nums_len - gap):
#             j = i
#             key = nums[j+gap]
#             while j >= 0 and key < nums[j]:
#                 nums[j+gap] = nums[j]
#                 j -= gap
#             nums[j+gap] = key
#         gap //= 2
#     return nums

# 2017.06.12
def shell_sort(nums):
    nums_len = len(nums)
    gap = nums_len // 2
    while gap > 0:
        for i in range(gap):
            for j in range(i+gap, nums_len, gap):
                current_num = nums[j]
                k = j - gap
                while k >= 0 and current_num < nums[k]:
                    nums[k+gap] = nums[k]
                    k -= gap
                nums[k+gap] = current_num
        gap = gap // 2
        
# 2017.06.12
def shell_sort(nums):
    nums_len = len(nums)
    gap = nums_len // 2
    while gap > 0:
        for j in range(nums_len - gap):
            current_num = nums[j]
            k = j - gap
            while k >= 0 and current_num < nums[k]:
                nums[k+gap] = nums[k]
                k -= gap
            nums[k+gap] = current_num
        gap = gap // 2


if __name__ == "__main__":
    nums = [randint(1,100) for _ in range(10)]
    print(nums)
    shell_sort(nums)
    print(nums)
