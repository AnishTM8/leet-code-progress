# Last updated: 6/29/2025, 12:03:44 AM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def backtrack(openedN, closedN):
            if openedN == closedN == n:
                res.append("".join(stack))
            
            if openedN < n:
                stack.append("(")
                backtrack(openedN + 1, closedN)
                stack.pop()
            
            if closedN < openedN:
                stack.append(")")
                backtrack(openedN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res