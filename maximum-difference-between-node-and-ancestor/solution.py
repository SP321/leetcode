# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=-inf
        def dfs(node,mx=-inf,mn=inf):
            nonlocal ans
            if not node:
                ans=max(ans,mx-mn)
                return
            mx=max(mx,node.val)
            mn=min(mn,node.val)
            dfs(node.left,mx,mn)
            dfs(node.right,mx,mn)
        dfs(root)
        return ans