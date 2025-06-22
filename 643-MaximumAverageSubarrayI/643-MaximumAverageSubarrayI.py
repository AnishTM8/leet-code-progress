# Last updated: 6/22/2025, 7:16:01 PM
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = 0

        
        for i in range(k):
            current_sum += nums[i]
                
        max_avg = current_sum / float(k)  # Use float conversion for division
                
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            avg = current_sum / float(k)  # Convert k to float
            max_avg = max(avg, max_avg)
            
        return max_avg
        
