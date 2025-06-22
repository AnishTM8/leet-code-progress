# Last updated: 6/22/2025, 7:16:16 PM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False