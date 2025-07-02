# Last updated: 7/2/2025, 5:23:06 PM
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b = 0, 1

        for i in range(2 , n + 1):
            a, b = b, b + a
        return b