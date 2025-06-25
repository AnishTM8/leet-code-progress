# Last updated: 6/25/2025, 9:42:55 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        divisor = 1
        while x >= divisor*10:
            divisor *= 10
        
        while x:
            if x%10 != x//divisor:
                return False
            x = (x%divisor) // 10
            divisor = divisor/100
        return True