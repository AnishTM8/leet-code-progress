# Last updated: 6/22/2025, 7:16:21 PM
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            while right > left and not self.isAlphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True
    
    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord("a") <= ord(c) <= ord("z") or ord('0') <= ord(c) <= ord('9')) 
