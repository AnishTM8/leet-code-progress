# Last updated: 3/11/2026, 8:27:15 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        def swap(i, j):
7            nums[i], nums[j] = nums[j], nums[i]
8
9        l, r = 0, len(nums) - 1
10        k = 0
11
12        while k <= r:
13            if nums[k] == 0:
14                swap(l, k)
15                l += 1
16            elif nums[k] == 2:
17                swap(k, r)
18                r -= 1
19                k -= 1
20            k += 1
21        
22