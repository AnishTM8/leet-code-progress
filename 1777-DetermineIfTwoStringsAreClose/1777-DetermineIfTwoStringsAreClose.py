# Last updated: 6/22/2025, 7:15:47 PM
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        count1 = Counter(word1)
        count2 = Counter(word2)

        sorted_values1 = sorted(count1.values())
        sorted_values2 = sorted(count2.values())

        keys_match = set(count1.keys()) == set(count2.keys())

        return sorted_values1 == sorted_values2 and keys_match