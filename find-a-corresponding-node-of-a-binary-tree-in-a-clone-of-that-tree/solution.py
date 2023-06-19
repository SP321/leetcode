# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(i,j):
            if i==target:
                return j
            if i.left:
                y=dfs(i.left,j.left)
                if y:
                    return y
            if i.right:
                y=dfs(i.right,j.right)
                if y:
                    return y
            return None
        return dfs(original,cloned)
        