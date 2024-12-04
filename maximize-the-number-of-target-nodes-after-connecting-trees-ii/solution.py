class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n=len(edges1)+1
        m=len(edges2)+1
        g=[[] for _ in range(n+m)]
        for u,v in edges1:
            g[u].append(v)
            g[v].append(u)

        g2=[[] for _ in range(n+m)]
        for u,v in edges2:
            g2[u].append(v)
            g2[v].append(u)


        ec=0
        oc=0
        color=[0]*n
        def dfs(u,par=None,r=0):
            nonlocal ec,oc
            if r==1:
                color[u]=1
                oc+=1
            else:
                ec+=1
            for v in g[u]:
                if v!=par:
                    dfs(v,u,1-r)
        dfs(0)

        ec2=0
        oc2=0
        def dfs2(u,par=None,r=0):
            nonlocal ec2,oc2
            if r==1:
                oc2+=1
            else:
                ec2+=1
            for v in g2[u]:
                if v!=par:
                    dfs2(v,u,1-r)
        dfs2(0)
       
        ans=[]
        c2=max(ec2,oc2)
        for i in range(n):
            ans.append(ec+c2 if color[i]==0 else oc+c2)
        return ans