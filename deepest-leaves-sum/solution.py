# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d=defaultdict(int)
        ma=0
        def dfs(i,x):
            nonlocal ma
            ma=max(ma,x)
            d[x]+=i.val
            if i.left:
                dfs(i.left,x+1)
            if i.right:
                dfs(i.right,x+1)
        dfs(root,0)
        return d[ma]
            
        