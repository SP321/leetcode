# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans=[]
        def dfs(node,par=None,left=True):
            if not node:
                return
            if node.val in to_delete:
                if par:
                    if left:
                        par.left=None
                    else:
                        par.right=None
                dfs(node.left,None,True)
                dfs(node.right,None,False)
            else:
                if par==None:
                    ans.append(node)
                dfs(node.left,node,True)
                dfs(node.right,node,False)
        dfs(root,None)
        return ans
