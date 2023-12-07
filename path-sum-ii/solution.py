# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def backtrack(node,path=[],s=0):
            if not node:
              return
            if not node.left and not node.right:
              if s+node.val==targetSum:
                  ans.append(path.copy()+[node.val])
            else:
              if node.left:
                backtrack(node.left,path+[node.val],s+node.val)
              if node.right:
                backtrack(node.right,path+[node.val],s+node.val)
        backtrack(root)
        return ans