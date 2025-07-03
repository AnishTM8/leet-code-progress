# Last updated: 7/3/2025, 10:55:05 AM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        max_len = max(len(word1), len(word2))
        res = ""

        for i in range(max_len):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res