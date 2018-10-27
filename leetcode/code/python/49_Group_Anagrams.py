"""49. Group Anagrams
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictStr = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in dictStr:
                dictStr[sorted_s] = [s]
            else:
                dictStr[sorted_s].append(s)
        return list(dictStr.values())
