# Last updated: 7/2/2025, 5:08:49 PM
class Solution:
    def reverse(self, x: int) -> int:
        max, min = 2**31, -2**31
        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10)

            if (res > max // 10 or (res == max //10 and digit >= max%10 )):
                return 0
            if (res < min // 10 or (res == min//10 and digit <= min%10)):
                return 0
            res = (res*10) + digit
        return res
