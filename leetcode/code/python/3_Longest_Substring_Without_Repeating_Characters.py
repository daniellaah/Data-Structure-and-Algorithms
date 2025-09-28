class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        last_seen = {}
        for r in range(len(s)):
            if s[r] in last_seen and last_seen[s[r]] >= l:
                l = last_seen[s[r]] + 1
            last_seen [s[r]] = r
            ans = max(ans, r - l + 1)
        return ans
