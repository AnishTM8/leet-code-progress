# Last updated: 6/22/2025, 7:16:33 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_map = {}

        for key, value in enumerate(nums):
            diff = target - value
            if diff in diff_map:
                return [diff_map[diff], key]
            diff_map[value] = key