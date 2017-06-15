'''给出一个具有重复数字的列表，找出列表所有不同的排列。
样例
给出列表 [1,2,2]，不同的排列有：

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
'''
# 方法一
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
            if i > 0 and nums[i-1] == nums[i]:
                continue
            self.search(nums[:i] + nums[i+1:], permutation + [nums[i]])
    def permuteUnique(self, nums):
        if nums is None:
            return []
        self.search(sorted(nums), [])
        return self.res
# 方法二
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    res = []
    def search(self, nums, permutation, used):
        if not nums:
            self.res.append(permutation)
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])
            self.search(nums[:i] + nums[i+1:], permutation + [nums[i]], set())
    def permuteUnique(self, nums):
        if nums is None:
            return []
        self.search(nums, [], set())
        return self.res
