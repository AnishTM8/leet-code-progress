# Last updated: 6/22/2025, 7:15:42 PM
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = []

        for char in s:
            if char != '*':
                output.append(char)
            else:
                # if output:
                    output.pop()
        return "".join(output)

