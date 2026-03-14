# Last updated: 3/14/2026, 3:37:00 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            m = (l + r) // 2
7
8            if nums[m] == target:
9                return m
10            elif nums[m] < target:
11                l = m + 1
12            else:
13                r = m - 1
14        
15        return l 
16