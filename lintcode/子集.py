class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    res = []
    def search(self, nums, subset):
        self.res.append(subset)
        for i in range(len(nums)):
            self.search(nums[i+1:], subset + [nums[i]])

    def subsets(self, S):
        if S is None:
            return None
        self.res = []
        self.search(sorted(S), [])
        return self.res
