# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(x, cur=0):
            if not x:
                return 0
            cur=cur*10 + x.val
            if x.left is None and x.right is None:
                return cur
            return dfs(x.left,cur)+dfs(x.right,cur)
        return dfs(root)