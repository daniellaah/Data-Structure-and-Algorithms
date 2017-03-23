"""125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            s_i, s_j = s[i].lower(), s[j].lower()
            if s_i.isalnum() and s_j.isalnum():
                i, j = i+1, j-1
                if s_i != s_j:
                    return False
            if not s_i.isalnum():
                i += 1
            if not s_j.isalnum():
                j -= 1
        return True
