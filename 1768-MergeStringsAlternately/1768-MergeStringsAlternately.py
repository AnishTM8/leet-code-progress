# Last updated: 7/3/2025, 10:59:41 AM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""
        gcd = math.gcd(len(str1), len(str2))

        return str1[:gcd]

