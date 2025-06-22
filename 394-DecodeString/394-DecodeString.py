# Last updated: 6/22/2025, 7:16:07 PM
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                k = ""

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substring)
        return "".join(stack)
