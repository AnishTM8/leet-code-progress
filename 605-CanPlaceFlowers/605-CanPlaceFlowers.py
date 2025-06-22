# Last updated: 6/22/2025, 7:16:02 PM
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """    
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and n != 0:
                prev = flowerbed[i-1] if i > 0 else 0
                nex = flowerbed[i+1] if i < len(flowerbed) - 1 else 0

                if prev == 0 and nex == 0:
                    flowerbed[i] = 1
                    n -= 1
        if n == 0:
            return True
        return False