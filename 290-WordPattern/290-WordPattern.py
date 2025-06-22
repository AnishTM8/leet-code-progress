# Last updated: 6/22/2025, 7:16:13 PM
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mapPS, mapSP = {}, {}

        string = s.split()

        if len(pattern) != len(string):
            return False
            
        for i in range(len(pattern)):
            c, w = pattern[i], string[i]

            if (c in mapPS and mapPS[c] != w) or (w in mapSP and mapSP[w] != c):
                return False
            mapPS[c]=w
            mapSP[w]=c
        return True