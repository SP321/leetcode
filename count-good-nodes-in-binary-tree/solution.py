# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, limit):
            if not node:
                return 0

            ans = 1 if node.val >= limit else 0
            limit = max(limit, node.val)
            ans += dfs(node.left, limit)+dfs(node.right, limit)
            return ans

        return dfs(root, root.val)
            
