class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        x=defaultdict(lambda :float('inf'))
        for u,v,w in roads:
            if x[u,v]>w:
                x[u,v]=w
                x[v,u]=w
        
        def floyd_warshall(nodes):
            y=defaultdict(lambda :float('inf'))
            for i in nodes:
                for j in nodes:
                    if i!=j:
                        y[i,j]=x[i,j]
            for k in nodes:
                for i in nodes:
                    for j in nodes:
                        y[i,j] = min(y[i,j],y[i,k]+y[k,j])
            return y
        valids={(i,) for i in range(n)}
        cur_valids={(i,) for i in range(n)}
        for _ in range(n+1):
            new_valids=set()
            for cur in cur_valids.copy(): 
                for j in range(n):
                    if j not in cur:
                        shortest=floyd_warshall(cur+(j,))
                        if all(shortest[k,j]<=maxDistance for k in cur):
                            new=list(cur)+[j]
                            new.sort()
                            new_valids.add(tuple(new))
            cur_valids=new_valids
            valids|=new_valids
        return len(valids)+1