# Last updated: 6/22/2025, 7:15:44 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        max_len = max(len(word1), len(word2))
        output = ''

        for i in range(max_len):
            if i < len(word1):
                output += word1[i]
            if i < len(word2):
                output += word2[i]

        return output