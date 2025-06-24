# Last updated: 6/23/2025, 11:57:34 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True
        return False