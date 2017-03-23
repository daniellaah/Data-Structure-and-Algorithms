"""Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 Notice

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.
"""
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
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
