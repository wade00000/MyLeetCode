1class Solution(object):
2    def searchInsert(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        new_list = nums[:]
9
10        if target in set(nums):
11           return  new_list.index(target)
12        else:
13            new_list.append(target)
14            asc = sorted(new_list)
15            return asc.index(target)
16
17        