# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=[root]
        ans=None
        while q:
            ans=q[0].val
            q2=[]
            for node in q:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q=q2
        return ans