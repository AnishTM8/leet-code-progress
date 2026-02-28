# Last updated: 2/28/2026, 10:46:55 AM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        ans = []
4
5        for i in range(2):
6            for num in nums:
7                ans.append(num)
8        
9        return ans