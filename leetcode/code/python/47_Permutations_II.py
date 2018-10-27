"""47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
# 解法一
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.ans = []
        self.recursive(nums, set(), [])
        return self.ans
    def recursive(self, nums, used, res):
        if not nums:
            self.ans.append(res)
        else:
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                else:
                    used.add(nums[i])
                    self.recursive(nums[:i]+nums[i+1:], set(), res+[nums[i]])
# 解法二
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.ans = []
        self.recursive(sorted(nums), [])
        return self.ans
    def recursive(self, nums, res):
        if not nums:
            self.ans.append(res)
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.recursive(nums[:i]+nums[i+1:], res+[nums[i]])
