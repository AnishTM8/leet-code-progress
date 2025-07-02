# Last updated: 7/1/2025, 9:39:55 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =="":
            return -1

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1