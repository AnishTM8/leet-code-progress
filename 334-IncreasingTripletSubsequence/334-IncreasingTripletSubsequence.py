# Last updated: 6/22/2025, 7:16:11 PM
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        a = float('inf')
        b = float('inf')

        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False