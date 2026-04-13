# Last updated: 4/13/2026, 1:25:27 PM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        l, r = 0, len(s) - 1
4
5        while l <= r:
6            if s[l] != s[r]:
7                skipL, skipR = s[l:r], s[l + 1: r + 1]
8                return (skipL == skipL[::-1] or skipR== skipR[::-1])
9            l += 1
10            r -= 1
11        return True
12
13