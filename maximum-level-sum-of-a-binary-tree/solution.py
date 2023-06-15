# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d=defaultdict(int)
        def dfs(i,x):
            d[x]+=i.val
            if i.left:
                dfs(i.left,x+1)
            if i.right:
                dfs(i.right,x+1)
        dfs(root,1)
        print(d)
        max_val = max(d.values())
        return next(i for i in d if d[i]==max_val)

        
            