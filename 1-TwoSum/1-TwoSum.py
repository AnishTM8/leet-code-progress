# Last updated: 6/25/2025, 11:44:53 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in diff_map:
                return [i, diff_map[diff]]
            
            diff_map[num] = i
    