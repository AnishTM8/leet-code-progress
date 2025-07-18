# Last updated: 6/22/2025, 7:16:06 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        sums = defaultdict(int)
        sums[0] = 1

        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                count = sums[total-targetSum]

                sums[total] += 1

                count += dfs(root.left, total) + dfs(root.right, total)

                sums[total] -= 1
            return count
        return dfs(root, 0)
        