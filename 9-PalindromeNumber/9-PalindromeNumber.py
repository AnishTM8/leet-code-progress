# Last updated: 7/3/2025, 3:08:10 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1

        while x >= div*10:
            div *= 10
        
        while x:
            if x%10 != x//div:
                return False
            x = (x%div)//10
            div = div/100
        return True

        