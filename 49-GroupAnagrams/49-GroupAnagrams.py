# Last updated: 6/24/2025, 8:48:28 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            res[tuple(sorted_s)].append(s)
        return list(res.values())