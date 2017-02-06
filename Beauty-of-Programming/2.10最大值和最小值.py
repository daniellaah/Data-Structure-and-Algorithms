from random_nums import random_nums
# 解法一: 同时比较两个数
def find_min_max_1(nums):
    min_num = max_num = nums[0]
    for i in range(0, len(nums) - len(nums) % 2, 2):
        if nums[i] > nums[i+1]:
            cur_max, cur_min = nums[i], nums[i+1]
        else:
            cur_max, cur_min = nums[i+1], nums[i]
        min_num = min(min_num, cur_min)
        max_num = max(max_num, cur_max)

    min_num = min(min_num, nums[-1])
    max_num = max(max_num, nums[-1])

    return min_num, max_num

# 解法二: 分治
def find_min_max_2(nums, left, right):
    if right - left > 2:
        mid = (left+right) // 2
        min_left, max_left = find_min_max_2(nums, left, mid)
        min_right, max_right = find_min_max_2(nums, mid, right)
        return min(min_left, min_right), max(max_left, max_right)
    else:
        return min(nums[left], nums[right-1]), max(nums[left], nums[right-1])



if __name__ == "__main__":
    nums = random_nums()
    print(nums)
    print(find_min_max_1(nums))
    print(find_min_max_2(nums, 0, len(nums)))
