class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        for i,j in pairwise(range(n)):
            g[i].append(j)
        ans=[]
       
        for u,v in queries:
            g[u].append(v)
            q=[0]
            visited=set(q)
            c=0
            while q:
                q2=[]
                for u in q:
                    if u==n-1:
                        q2=[]
                        break
                    for v in g[u]:
                        if v not in visited:
                            q2.append(v)
                            visited.add(v)
                q=q2
                c+=1
            ans.append(c-1)
        return ans