# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val=0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if root.right:
            self.convertBST(root.right)
        root.val=self.val=self.val+root.val
        if root.left:
            self.convertBST(root.left)
        return root
