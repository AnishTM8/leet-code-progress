# Last updated: 6/22/2025, 7:16:14 PM
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right]:
                nums[left],nums[right] = nums[right], nums[left]
                left += 1
        return nums
                
