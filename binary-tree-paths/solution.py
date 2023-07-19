# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def dfs(i,path):
            if not i.left and not i.right:
                ans.append("->".join(str(x) for x in path+[i.val]))
            if i.left:
                dfs(i.left,path+[i.val])
            if i.right:
                dfs(i.right,path+[i.val])
        dfs(root,[])
        return ans