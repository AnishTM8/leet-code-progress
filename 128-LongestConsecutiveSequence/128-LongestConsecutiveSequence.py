# Last updated: 6/25/2025, 5:52:26 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        output = 0

        for num in numSet:
            if num-1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                output = max(output, length)
        return output