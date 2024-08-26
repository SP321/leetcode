"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans=[]
        def dfs(node):
            if not node:
                return
            for n2 in node.children:
                dfs(n2)
            ans.append(node.val)
        dfs(root)
        return ans