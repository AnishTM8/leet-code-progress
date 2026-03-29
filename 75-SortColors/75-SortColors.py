# Last updated: 3/29/2026, 10:14:52 AM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        l, r = 0, len(nums) - 1
7        k = 0
8
9        while k <= r:
10            if nums[k] == 0:
11                nums[l],nums[k] = nums[k], nums[l]
12                l += 1
13            elif nums[k] == 2:
14                nums[r], nums[k] = nums[k], nums[r]
15                r -= 1
16                k -= 1
17            k += 1
18        