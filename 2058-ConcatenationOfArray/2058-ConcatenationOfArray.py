# Last updated: 3/18/2026, 9:03:49 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
            for num in nums:
                ans.append(num)
        
        return ans