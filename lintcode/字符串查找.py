# 对于一个给定的 source 字符串和一个 target 字符串，
# 你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

class Solution:
    """
    @param: : source string to be scanned.
    @param: : target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if source is None or target is None or len(target) > len(source):
            return -1
        if target == '':
            return 0
        len_source, len_target = len(source), len(target)
        for i in range(len_source - len_target + 1):
            if target == source[i:i+len_target]:
                return i
        return -1
