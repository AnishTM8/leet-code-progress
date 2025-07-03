# Last updated: 7/3/2025, 11:28:36 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        return " ".join(words[::-1])