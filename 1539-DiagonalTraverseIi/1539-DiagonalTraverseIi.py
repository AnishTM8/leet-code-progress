# Last updated: 6/22/2025, 7:15:50 PM
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        diagonals = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])
        
        result = []
        for key in sorted(diagonals.keys()):
            result.extend(diagonals[key][::-1])
        
        return result


        
        