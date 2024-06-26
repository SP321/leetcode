# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals=[]
        def inorder(node):
            nonlocal vals
            if not node:
                return
            inorder(node.left)
            vals.append(node)
            inorder(node.right)
        def helper(l,r):
            if l==r:
                return None
            m=l+(r-l)//2
            vals[m].left=helper(l,m)
            vals[m].right=helper(m+1,r)
            return vals[m]
        inorder(root)
        return helper(0,len(vals))