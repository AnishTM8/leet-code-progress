# Last updated: 7/3/2025, 11:18:46 AM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and n!= 0:
                prev = flowerbed[i - 1] if i > 0 else 0
                nex = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
                if prev == 0 and nex == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n<=0