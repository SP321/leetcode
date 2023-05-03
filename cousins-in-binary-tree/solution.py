# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        l={}
        p={}
        p[root]=0
        def dfs(i,a):
            l[i.val]=a
            if i.left:
                p[i.left.val]=i.val
                dfs(i.left,a+1)
            if i.right:
                p[i.right.val]=i.val
                dfs(i.right,a+1)
        dfs(root,0)
        return l[x]==l[y] and p[x]!=p[y]
