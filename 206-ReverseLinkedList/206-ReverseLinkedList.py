# Last updated: 6/23/2025, 11:54:22 PM
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