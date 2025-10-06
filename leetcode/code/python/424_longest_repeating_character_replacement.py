# https://leetcode.com/problems/longest-repeating-character-replacement/


class SolutionWithMaxCount:
    """
    Sliding window approach with frequency array and max(count) call.
    Time Complexity: O(n * 26) = O(n)
    Space Complexity: O(26) = O(1)

    Note: Calls max(count) every iteration which adds O(26) overhead.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        count = [0] * 26
        left = 0

        for right, char in enumerate(s):
            count[ord(char) - ord("A")] += 1

            # Window is valid if: window_size - most_frequent_char <= k
            while (right - left + 1) - max(count) > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


class Solution:
    """
    Optimized sliding window with cached max frequency.
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key insight: We don't need to update max_count when shrinking the window
    because we only care about finding a longer valid window.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        count = [0] * 26
        max_count = 0
        left = 0

        for right, char in enumerate(s):
            count[ord(char) - ord("A")] += 1
            max_count = max(max_count, count[ord(char) - ord("A")])

            # If window is invalid, shrink from left
            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length