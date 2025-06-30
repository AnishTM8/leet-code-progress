# Last updated: 6/30/2025, 3:18:08 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol =[], []

        def backtrack(openedN, closedN):
            if openedN == closedN == n:
                res.append("".join(sol))
            
            if openedN < n:
                sol.append("(")
                backtrack(openedN + 1, closedN)
                sol.pop()
            
            if closedN < openedN:
                sol.append(")")
                backtrack(openedN, closedN + 1)
                sol.pop()
            
        backtrack(0,0)
        return res