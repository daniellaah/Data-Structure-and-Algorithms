"""Rotate String
Given a string and an offset, rotate string by offset. (rotate from left to right)

Example
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
"""
class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
	    # write you code here
	    if not s or offset < 0:
	        return None
	    length = len(s)
	    offset %= length
	    s[:] = s[-offset:] + s[:-offset]
