# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev=float("-inf")
        ans=float('inf')
        def inorder(node):
            nonlocal ans,prev
            if node.left:
                inorder(node.left)
            cur=node.val
            ans=min(ans,abs(cur-prev))
            prev=cur
            if node.right:
                inorder(node.right)
        inorder(root)
        return ans