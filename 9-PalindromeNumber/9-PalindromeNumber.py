# Last updated: 6/25/2025, 9:44:29 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        
        # divisor = 1
        # while x >= divisor*10:
        #     divisor *= 10
        
        # while x:
        #     if x%10 != x//divisor:
        #         return False
        #     x = (x%divisor) // 10
        #     divisor = divisor/100
        # return True

        s = str(x)

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True