# Last updated: 6/30/2025, 12:25:02 AM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #Store Pair: [index(0), temprature(1)]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]: # get the top element
                index, temp = stack.pop()
                res[index] = (i - index)
            stack.append([i,t])
        return res