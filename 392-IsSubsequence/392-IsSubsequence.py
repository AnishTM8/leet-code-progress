# Last updated: 6/22/2025, 7:16:07 PM
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_pointer = 0
        t_pointer = 0

        while t_pointer < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1
            
        return s_pointer == len(s)
