# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        is_odd = False
        while q:
            q2 = []
            prev = None
            for node in q:
                if is_odd:
                    if node.val % 2 or (prev and prev.val <= node.val):
                        return False
                else:
                    if not node.val % 2 or (prev and prev.val >= node.val):
                        return False
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
                prev = node
            q = q2
            is_odd = not is_odd
        return True