# Last updated: 4/6/2026, 5:56:06 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        count = defaultdict(int)
4
5        for n in nums:
6            count[n] += 1
7
8            if len(count) <= 2:
9                continue
10            
11            new_count = defaultdict(int)
12
13            for n,c in count.items():
14                if c > 1:
15                    new_count[n] = c - 1
16            
17            count = new_count
18        
19        res = []
20        for n in count:
21            if nums.count(n) > len(nums) // 3:
22                res.append(n)
23        
24        return res