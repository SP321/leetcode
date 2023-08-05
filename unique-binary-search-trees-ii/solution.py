# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(start, end):
            ans = []
            if start > end:
                ans.append(None)
                return ans
            for i in range(start, end + 1):
                leftSubtrees = helper(start, i - 1)
                rightSubtrees = helper(i + 1, end)
                
                for left in leftSubtrees:
                    for right in rightSubtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans
        return helper(1, n)
   