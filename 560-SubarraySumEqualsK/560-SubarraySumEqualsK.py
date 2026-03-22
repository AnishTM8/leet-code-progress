# Last updated: 3/22/2026, 2:37:12 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        res = 0
4        curSum = 0
5        prefix = {0 : 1}
6
7        for num in nums:
8            curSum += num
9            diff = curSum - k
10
11            res += prefix.get(diff, 0)
12            prefix[curSum] = 1 + prefix.get(curSum, 0)
13        
14        return res
15