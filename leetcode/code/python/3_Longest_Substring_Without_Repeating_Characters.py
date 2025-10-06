# LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    """
    Sliding window approach with hash map.
    Time Complexity: O(n)
    Space Complexity: O(min(n, m)) where m is the charset size
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        char_index = {}

        for right, char in enumerate(s):
            # If character was seen and is within current window
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length