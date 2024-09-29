# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=[root]
        c=0
        while q:
            q2=[]
            for node in q:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if c&1:
                for i in range(len(q)//2):
                    q[i].val,q[~i].val=q[~i].val,q[i].val
            q=q2
            c+=1
        return root