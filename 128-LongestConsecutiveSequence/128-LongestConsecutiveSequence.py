# Last updated: 6/22/2025, 7:16:20 PM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        output = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                output = max(output, length)
        return output
