# Last updated: 3/19/2026, 6:43:39 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        res = 0
5    
6        for num in num_set:
7            if num - 1 not in num_set:
8                length = 0
9                while num + length in num_set:
10                    length += 1
11
12                res = max(res, length)
13        return res