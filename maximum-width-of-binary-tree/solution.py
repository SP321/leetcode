# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        m={}
        m[root]=0
        x=[root]
        while len(x)>0:
            i=0;
            y=[]
            minp=0
            while i<len(x):
                a=x[i]
                if a.left:
                    minp=m[a]*2
                    break
                if a.right:
                    minp=m[a]*2+1
                    break
                i+=1
            while i<len(x):
                a=x[i]
                if a.left:
                    m[a.left]=m[a]*2-minp
                    y.append(a.left)
                    ans=max(ans,m[a.left])
                if a.right:
                    m[a.right]=m[a]*2+1-minp
                    y.append(a.right)
                    ans=max(ans,m[a.right])
                i+=1
            x=y
        return ans+1;
                    
            