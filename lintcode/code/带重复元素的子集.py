class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    res = []
    def search(self, nums, subset):
        self.res.append(subset)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.search(nums[i+1:], subset + [nums[i]])

    def subsetsWithDup(self, S):
        if S is None:
            return None
        self.search(sorted(S), [])
        return self.res
