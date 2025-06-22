# Last updated: 6/22/2025, 7:16:32 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        div = 1
        while x >= 10*div: #finds the number in required for the divisor
            div *= 10

        while x:
            if x//div != x%10: #x//div give first number and x%10 gives last number
                return False
            x = (x%div) // 10
            div = div / 100
        
        return True