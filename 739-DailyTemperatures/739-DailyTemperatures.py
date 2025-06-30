# Last updated: 6/30/2025, 3:21:18 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair(i, t)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append([i,t])
        return res