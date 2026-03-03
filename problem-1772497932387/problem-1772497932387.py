# Last updated: 3/2/2026, 5:32:12 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False 
5
6        sCount, tCount = {}, {}
7
8        for i in range(len(s)):
9            sCount[s[i]] = 1 + sCount.get(s[i], 0)
10            tCount[t[i]] = 1 + tCount.get(t[i], 0)
11
12        return sCount == tCount        
13