# Last updated: 3/12/2026, 5:48:11 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count = {}
4        freq = [[] for i in range(len(nums) + 1)]
5
6        for num in nums:
7            count[num] = 1 + count.get(num, 0)
8        
9        for num, cnt in count.items():
10            freq[cnt].append(num)
11        
12        res = []
13        for i in range(len(freq) - 1, 0, -1):
14            for num in freq[i]:
15                res.append(num)
16                if k == len(res):
17                    return res
18