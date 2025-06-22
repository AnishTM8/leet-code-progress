# Last updated: 6/22/2025, 7:15:49 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxVal):
            if not node:
                return 0
            output = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)

            output += dfs(node.left, maxVal)
            output += dfs(node.right, maxVal)
            return output
        
        return dfs(root, root.val)