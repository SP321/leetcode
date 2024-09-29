# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        q=[root]
        depth=0
        while q:
            q2=[]
            for x in q:
                if x.left:
                    q2.append(x.left)
                if x.right:
                    q2.append(x.right)
            q=q2
            depth+=1
        ans=[]
        sz=( (1<<depth) -1)
        pos=sz//2
        q=[(root,pos)]
        depth-=1
        while q:
            row=[ "" for _ in range(sz) ]
            depth-=1
            q2=[]
            for x,pos in q:
                row[pos]=str(x.val)
                if x.left:
                    q2.append( (x.left,pos- (1<<depth)) )
                if x.right:
                    q2.append( (x.right,pos+ (1<<depth)) )
            ans.append(row)
            q=q2
        return ans