# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        a=[]
        q=[root] if root else []
        while q:
            a.append([i.val for i in q])
            q2=[]
            for node in q:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q=q2
        def swaprev(a):
            l=0
            r=len(a)-1
            while l<r:
                a[l],a[r]=a[r],a[l]
                l+=1
                r-=1
            return a
        return swaprev(a)