# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        x=defaultdict(int)
        def dfs(node,level=0):
            nonlocal x
            if node:
                x[level]=node.val
                dfs(node.left,level+1)
                dfs(node.right,level+1)
        dfs(root)
        return x.values()
        