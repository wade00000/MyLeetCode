1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        L = 1
8        for R in range(1,len(nums)):
9            if nums[R] != nums[R-1]:
10                nums[L] = nums[R]
11                L += 1
12        return L
13                
14            
15