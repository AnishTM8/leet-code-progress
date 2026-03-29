# Last updated: 3/29/2026, 12:00:39 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count = {}
4        freq = [[] for i in range(len(nums) + 1)]
5
6        for num in nums:
7            count[num] = 1 + count.get(num, 0)
8        
9        for n,c in count.items():
10            freq[c].append(n)
11        
12        res = []
13        for i in range(len(freq) - 1, -1, -1):
14            for n in freq[i]:
15                res.append(n)
16                if len(res) == k:
17                    return res
18            