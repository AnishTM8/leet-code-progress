# Last updated: 6/22/2025, 7:15:48 PM
class Solution(object):
    def maxVowels(self, s, k):
        """:type s: str
        :type k: int
        :rtype: int
        """ 
        count = 0
        vowels = {'a','e','i','o','u'}

        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count +=1
            if s[i-k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        return max_count