# Last updated: 3/23/2026, 5:32:47 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        for i in range(len(nums)):
4            if nums[i] < 0:
5                nums[i] = 0
6        
7        for i in range(len(nums)):
8            val = abs(nums[i])
9
10            if 1<=val<=len(nums):
11                if nums[val - 1] > 0:
12                    nums[val - 1] *= -1
13                elif nums[val - 1] == 0:
14                    nums[val-1] = -1 * (1 + len(nums))
15            
16        for i in range(1, len(nums) + 1):
17            if nums[i - 1] >= 0:
18                return i
19        return len(nums) + 1
20