# Last updated: 3/6/2026, 2:02:56 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k = 0
4
5        for i in range(len(nums)):
6            if nums[i] != val:
7                nums[k] = nums[i]
8                k += 1
9        return k
10            