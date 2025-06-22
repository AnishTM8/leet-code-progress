# Last updated: 6/22/2025, 7:16:23 PM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            res[tuple(sorted_s)].append(s) 
        return res.values()
