# Last updated: 3/21/2026, 2:15:14 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        count = {}
4
5        for num in nums:
6            count[num] = 1 + count.get(num, 0)
7        
8        res = []
9
10        for n,c in count.items():
11            if c > len(nums) // 3:
12                res.append(n)        
13        return res
14