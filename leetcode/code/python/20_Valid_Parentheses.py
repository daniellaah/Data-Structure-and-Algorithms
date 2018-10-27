"""20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Subscribe to see which companies asked this question.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {')':'(', ']':'[', '}':'{' }
        for symbol in s:
            if symbol in parentheses.values():
                stack.append(symbol)
            else:
                if len(stack) < 1:
                    return False
                if parentheses[symbol] != stack.pop():
                    return False
        return not stack
