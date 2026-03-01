# Last updated: 3/1/2026, 3:54:34 AM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4
5        for i in range(len(nums)):
6            if nums[i] in seen:
7                return True
8            seen.add(nums[i])
9        return False