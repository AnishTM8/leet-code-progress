# Last updated: 3/5/2026, 5:36:30 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        res = defaultdict(list)
4
5        for s in strs:
6            sorted_s = sorted(s)
7            res[tuple(sorted_s)].append(s)
8        return list(res.values())