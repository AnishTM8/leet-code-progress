# Last updated: 6/22/2025, 7:15:46 PM
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output = 0
        nums.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                output += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return output

                
            

