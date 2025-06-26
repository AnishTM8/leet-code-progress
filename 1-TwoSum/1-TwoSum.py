# Last updated: 6/26/2025, 10:20:27 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in diff_map:
                return [diff_map[diff], i]

            diff_map[num] = i
        