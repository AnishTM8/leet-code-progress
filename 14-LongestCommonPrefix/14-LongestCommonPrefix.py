# Last updated: 3/4/2026, 3:38:20 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        res = ""
4
5        for i in range(len(strs[0])):
6            for word in strs:
7                if i == len(word) or word[i] != strs[0][i]:
8                    return res
9            
10            res += strs[0][i]
11        
12        return res
13