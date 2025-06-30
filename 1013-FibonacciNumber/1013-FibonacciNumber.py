# Last updated: 6/30/2025, 12:26:10 AM
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, b + a
        return b