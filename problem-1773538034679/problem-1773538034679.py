# Last updated: 3/14/2026, 7:27:14 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3
4        for i in range(len(digits) - 1, -1, -1):
5            if digits[i] < 9:
6                digits[i] += 1
7                return digits
8            else:
9                digits[i] = 0
10        
11        return [1] + digits