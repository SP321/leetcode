# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth_sum={}
        depth_map={}
        sibling={}
        def dfs(i,x):
            if x not in depth_sum:
                depth_sum[x]=0
                depth_map[x]=[]
            depth_sum[x]+=i.val
            depth_map[x].append(i)
            if i.left:
                sibling[i.left]=i.right
                dfs(i.left,x+1)
            if i.right:
                sibling[i.right]=i.left
                dfs(i.right,x+1)
        dfs(root,0)
        sibling[root]=False
        for i in depth_sum:
            newval={}
            for cur in depth_map[i]:
                val=depth_sum[i]-cur.val
                if sibling[cur]:
                    val-=sibling[cur].val
                newval[cur]=val
            for cur in depth_map[i]:
                cur.val=newval[cur]
        return root
            

