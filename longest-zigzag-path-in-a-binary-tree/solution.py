# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigzag(root,val,direction):
            if root is None:
                return val
            if direction:
                return max(zigzag(root.left,val+1,False),zigzag(root.right,1,True))
            else:
                return max(zigzag(root.right,val+1,True),zigzag(root.left,1,False)) 
        return max(zigzag(root,0,True),zigzag(root,0,False))-1