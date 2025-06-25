# Last updated: 6/24/2025, 8:29:14 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False