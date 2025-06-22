# Last updated: 6/22/2025, 7:16:19 PM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = split(s)

        return " ".join(words[::-1])