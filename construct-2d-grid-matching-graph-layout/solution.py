class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        deg = Counter()
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u]+=1
            deg[v]+=1

        node = None
        corners=set()
        mn=inf
        for x in g:
            if len(g[x])<mn:
                node=x
                mn=len(g[x])
                
        for x in g:
            g[x].sort(key=deg.get)
            if len(g[x])==mn:
                corners.add(x)

        row=[node]
        visited=set([node])
        while row[-1]==node or row[-1] not in corners:
            for nei in g[row[-1]]:
                if nei not in visited:
                    visited.add(nei)
                    row.append(nei)
                    break
        ans=[row]
        c=len(row)
        r=n//len(row)
        for _ in range(1,r):
            row=[]
            for j in range(c):
                for nei in g[ans[-1][j]]:
                    if nei not in visited:
                        visited.add(nei)
                        row.append(nei)
                        break
            ans.append(row)
        return ans