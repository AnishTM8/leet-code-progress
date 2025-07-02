# Last updated: 7/2/2025, 5:21:48 PM
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