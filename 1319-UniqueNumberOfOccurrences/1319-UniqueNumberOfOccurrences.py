# Last updated: 6/22/2025, 7:15:53 PM
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = Counter(arr)

        checker = []

        for count in counts.values():
            if count in checker:
                return False
            checker.append(count)
        return True
