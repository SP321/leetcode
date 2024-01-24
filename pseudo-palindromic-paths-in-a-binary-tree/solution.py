# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def solve( root, count = 0):
            if not root:
                return 0
            count ^= 1 << (root.val - 1)
            res = solve(root.left, count) + solve(root.right, count)
            if root.left == root.right:
                if count & (count - 1) == 0:
                    res += 1
            return res
        return solve(root)



