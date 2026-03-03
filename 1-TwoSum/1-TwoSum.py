# Last updated: 3/3/2026, 7:27:14 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4
5        for i, n in enumerate(nums):
6            diff = target - n
7
8            if diff in seen:
9                return [seen[diff], i]
10
11            seen[n] = i
12        return