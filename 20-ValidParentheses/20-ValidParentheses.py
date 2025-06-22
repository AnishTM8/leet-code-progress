# Last updated: 6/22/2025, 7:16:28 PM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        close_open = {")":"(" ,"}":"{" ,"]":"["}

        for par in s:
            if par in close_open:
                if stack and close_open[par] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        return True if not stack else False