# Last updated: 3/19/2026, 6:39:45 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if len(nums) == 0:
4            return 0
5
6        num_set = set(nums)
7        res = 0
8        
9
10        for num in num_set:
11            if num - 1 not in num_set:
12                length = 1
13
14                while num + length in num_set:
15                    length += 1
16
17                res = max(res, length)
18    
19        return res