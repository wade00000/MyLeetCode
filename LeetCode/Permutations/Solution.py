1class Solution(object):
2    def permute(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        from itertools import permutations
8
9        return list(permutations(nums))
10
11        