# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.helper(1, n)
    
    def helper(self, start: int, end: int) -> List[Optional[TreeNode]]:
        result = []
        if start > end:
            result.append(None)
            return result
        
        for i in range(start, end + 1):
            leftSubtrees = self.helper(start, i - 1)
            rightSubtrees = self.helper(i + 1, end)
            
            for left in leftSubtrees:
                for right in rightSubtrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)
        
        return result