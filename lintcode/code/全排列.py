"""给定一个数字列表，返回其所有可能的排列。
样例
给出一个列表[1,2,3]，其全排列为：

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    res = []
    def search(self, nums, permutation):
        if not nums:
            self.res.append(permutation)
        for i in range(len(nums)):
            self.search(nums[:i] + nums[i+1:], permutation + [nums[i]])
    def permute(self, nums):
        if nums is None:
            return []
        self.search(nums, [])
        return self.res
