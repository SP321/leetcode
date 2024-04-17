# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans=[27]
        def dfs(node,pre):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans=min(ans,[node.val]+pre)
                return
            dfs(node.left,[node.val]+pre)
            dfs(node.right,[node.val]+pre)
        dfs(root,[])
        return ''.join([chr(97+x) for x in ans])