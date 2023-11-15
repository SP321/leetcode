# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        @cache
        def helper(root):
            if not root:
                return None,None
            tail=root
            
            left_head,left_tail=helper(root.left)
            right_head,right_tail=helper(root.right)

            if left_tail is not None:
                tail.right=left_head
                tail=left_tail
            if right_tail is not None:
                tail.right=right_head
                tail=right_tail
            root.left=None
            return root,tail
        return helper(root)[0]
                