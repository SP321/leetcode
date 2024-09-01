# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            a.append(node.val)
            dfs(node.right)
        dfs(root)
        a.sort(reverse=True)
        def dfs2(node):
            if not node:
                return
            dfs2(node.left)
            node.val=a.pop()
            dfs2(node.right)
        dfs2(root)
        
        