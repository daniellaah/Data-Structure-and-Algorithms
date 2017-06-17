'''面试题4：二维数组中的查找
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
整数，判断数组中是否含有该整数。
'''
# 判断右上角的数字与target的大小
def find_num(nums, target):
    if not nums or not target:
        return None
    row, col = 0, len(nums[0]) - 1
    while (row <= len(nums) - 1) and (col >= 0):
        if nums[row][col] == target:
            return (row, col)
        elif nums[row][col] > target:
            col -= 1
        else:
            row += 1
    return None

if __name__ == "__main__":
    nums = [[1, 2, 8, 9],
            [2, 4, 9, 12],
            [4, 7, 10, 13],
            [6, 8, 11, 15]]
    target = 11
    print(find_num(nums, target))
