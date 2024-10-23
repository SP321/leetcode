# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=[(root,0)]
        while q:
            q2=[]
            total=0
            d=Counter()
            for node,par in q:
                total+=node.val
                d[par]+=node.val
            for node,par in q:
                if node.left:
                    q2.append( (node.left,node) )
                if node.right:
                    q2.append( (node.right,node) )
                node.val=total-d[par]
            q=q2
        return root
            