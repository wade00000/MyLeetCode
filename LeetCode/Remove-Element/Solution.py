1class Solution(object):
2    def removeElement(self, nums, val):
3        """
4        :type nums: List[int]
5        :type val: int
6        :rtype: int
7        """
8        if not nums:
9            return 0
10
11        L = 0
12        for R in range(len(nums)):
13            if nums[R] != val:
14                nums[L] = nums[R]
15                L += 1
16        return L
17        
18        