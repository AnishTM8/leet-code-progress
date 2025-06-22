# Last updated: 6/22/2025, 7:15:48 PM
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = 0
        left = 0
        max_width = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            width = right - left 
            max_width = max(max_width, width)
        return max_width