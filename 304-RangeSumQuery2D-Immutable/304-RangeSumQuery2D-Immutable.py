# Last updated: 3/30/2026, 9:07:05 PM
1class NumMatrix:
2
3    def __init__(self, matrix: List[List[int]]):
4        ROWS, COLS = len(matrix), len(matrix[0])
5        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]
6
7        for r in range(ROWS):
8            prefix = 0
9            for c in range(COLS):
10                prefix += matrix[r][c]
11                above = self.sumMat[r][c + 1]
12                self.sumMat[r + 1][c + 1] = prefix + above
13
14    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
15        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
16        bottomRight = self.sumMat[r2][c2]
17        left = self.sumMat[r2][c1 - 1]
18        topLeft = self.sumMat[r1 - 1][c1 - 1]
19        above = self.sumMat[r1 - 1][c2]
20
21        return bottomRight - above - left + topLeft
22
23# Your NumMatrix object will be instantiated and called as such:
24# obj = NumMatrix(matrix)
25# param_1 = obj.sumRegion(row1,col1,row2,col2)