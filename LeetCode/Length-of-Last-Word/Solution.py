1class Solution(object):
2    def lengthOfLastWord(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        return len(s.split()[-1])
8        