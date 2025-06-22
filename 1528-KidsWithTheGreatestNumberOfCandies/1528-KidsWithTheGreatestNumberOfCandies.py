# Last updated: 6/22/2025, 7:15:51 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = [False for i in range(len(candies))]

        max_candies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res[i] = True
        return res