# Last updated: 6/22/2025, 7:15:56 PM
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zeros = 0
        max_width = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            width = right - left + 1
            max_width = max(max_width, width)
        return max_width 
            