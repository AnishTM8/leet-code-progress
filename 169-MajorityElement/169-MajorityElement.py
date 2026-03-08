# Last updated: 3/7/2026, 7:52:21 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        res, count = 0, 0
4
5        for num in nums:
6            if count == 0:
7                res = num
8            
9            count += (1 if num == res else -1)
10        
11        return res