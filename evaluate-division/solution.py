class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d={}
        for (x,y),z in zip(equations,values):
            if x not in d:
                d[x]=[]
            if y not in d:
                d[y]=[]
            d[x].append((y,z))
            d[y].append((x,1/z))
        seen={}
        def dfs(i,j,prod):
            if i not in seen or j not in seen or seen[i]:
                return -1
            seen[i]=True
            if i==j:
                return prod
            elif len(d[i])==0:
                return -1
            ans=-1
            for a,b in d[i]:
                ans=max(ans,dfs(a,j,prod*b))
            return ans
        ans=[]
        for x,y in queries:
            for i in d:
                seen[i]=False
            ans.append(dfs(x,y,1))
        return ans
            
