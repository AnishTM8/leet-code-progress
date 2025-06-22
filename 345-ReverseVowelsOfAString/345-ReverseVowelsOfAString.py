# Last updated: 6/22/2025, 7:16:10 PM
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels = "aeiouAEIOU"
        vowel = []

        for i in range(len(s)):
            if s_list[i] in vowels:
                vowel.append(s_list[i])
            
        for i in range(len(s)):
            if s_list[i] in vowels:
                s_list[i] = vowel.pop()

        return "".join(s_list)
            
