# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def dfs(node):
            if not node.left and not node.right:
                ans.append(1)
                return 1
            if node.left and node.right:
                a=dfs(node.left)
                b=dfs(node.right)
                if a==b and a>0:
                    ans.append(a+b+1)
                    return a+b+1
                return -1
            else:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                return -1
            
        dfs(root)
        ans.sort()
        if len(ans)<k:
            return -1
        return ans[-k]
        

