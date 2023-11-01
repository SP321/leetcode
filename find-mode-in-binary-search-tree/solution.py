# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d=defaultdict(int)
        def dfs(node):
            if not node:
                return
            d[node.val]+=1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        d2=defaultdict(list)
        for a,b in d.items():
            d2[b].append(a)
        return d2[max(d2)]