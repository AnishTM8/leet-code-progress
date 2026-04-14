# Last updated: 4/13/2026, 9:17:18 PM
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        """
4        :type word1: str
5        :type word2: str
6        :rtype: str
7        """
8        i, j = 0, 0
9        res = ""
10
11        while i < len(word1) and j < len(word2):
12            res += word1[i]
13            res += word2[j]
14            i += 1
15            j += 1
16        
17        res += word1[i:]
18        res += word2[j:]
19
20        return res