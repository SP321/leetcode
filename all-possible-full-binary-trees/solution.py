# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0: [], 1: [TreeNode(0)]}
        def trees(n):
            if n not in dp:
                ans = []
                for x in range(n):
                    y = n - 1 - x
                    for left in trees(x):
                        for right in trees(y):
                            node  = TreeNode(0)
                            node.left  = left
                            node.right = right
                            ans.append(node)
                dp[n] = ans
            return dp[n]
        return trees(n)