# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:
                return (0,0)
            l,lc=dfs(node.left)
            r,rc=dfs(node.right)
            s,c=l+r+node.val,lc+rc+1
            if s//c==node.val:
                ans+=1
            return s,c
        dfs(root)
        return ans