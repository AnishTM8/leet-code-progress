# Last updated: 3/21/2026, 2:33:14 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        count = defaultdict(int)
4
5        for num in nums:
6            count[num] += 1 
7
8            if len(count) <= 2:
9                continue
10            
11            new_count = defaultdict(int)
12            for n,c in count.items():
13                if c > 1:
14                    new_count[n] = c - 1
15            
16            count = new_count
17        
18        res = []
19
20        for n in count:
21            if nums.count(n) > len(nums)//3:
22                res.append(n)
23        return res
24                