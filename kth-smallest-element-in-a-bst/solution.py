# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: 'TreeNode', k: int) -> int:
        def inorder(node):
            nonlocal k
            if not node:
                return -1
            
            left = inorder(node.left)
            if left != -1:
                return left

            k -= 1
            if k == 0:
                return node.val

            return inorder(node.right)
        
        return inorder(root)