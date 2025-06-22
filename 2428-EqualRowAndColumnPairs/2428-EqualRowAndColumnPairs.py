# Last updated: 6/22/2025, 7:15:42 PM
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        transposed = list(zip(*grid))
        count = 0

        for i in range(len(transposed)):
            for j in range(len(grid)):
                if grid[j] == list(transposed[i]):
                    count += 1

        return count