# LeetCode: https://leetcode.com/problems/subarray-sum-equals-k/description/

from typing import List
from collections import defaultdict


class Solution:
    """
    Prefix sum with hash map approach.
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key insight: If prefix_sum[j] - prefix_sum[i] = k, then subarray[i+1:j+1] sums to k.
    We use a hash map to count occurrences of each prefix sum.
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # Base case: empty prefix has sum 0

        for num in nums:
            prefix_sum += num

            # Check if there exists a previous prefix such that:
            # prefix_sum - previous_prefix = k
            count += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] += 1

        return count