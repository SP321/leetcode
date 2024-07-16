# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        par={}
        depth={}
        q=[root]
        a,b=None,None
        d=0
        while (a==None or b==None):
            q2=[]
            for x in q:
                depth[x]=d
                if x.val==startValue:
                    a=x
                if x.val==destValue:
                    b=x
                if x.left:
                    q2.append(x.left)
                    par[x.left]=x
                if x.right:
                    q2.append(x.right)
                    par[x.right]=x
            q=q2
            d+=1
        c=0
        st=[]
        while a!=b:
            if depth[a]<depth[b]:
                if par[b].left==b:
                    st.append("L")
                else:
                    st.append("R")
                b=par[b]
            elif depth[b]<depth[a]:
                a=par[a]
                c+=1
            else:
                if par[b].left==b:
                    st.append("L")
                else:
                    st.append("R")
                b=par[b]
                a=par[a]
                c+=1
        ans="U"*c + ''.join(st[::-1])
        return ans
