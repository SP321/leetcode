class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g=defaultdict(list)
        for i,(u,v,w) in enumerate(edges):
            g[u].append((v,w,i))
            g[v].append((u,w,i))


        rev = defaultdict(set)

        def dijkstras(start,end):
            h = [(0,start)]
            dist = {start: 0}
            while h:
                cost, cur = heapq.heappop(h)
                if dist[cur] != cost:
                    continue
                if cur == end:
                    return cost
                for o, w, i in g[cur]:
                    if dist.get(o, inf) > cost + w:
                        dist[o] = cost + w
                        heapq.heappush(h, (cost + w, o))
                        rev[o]={i}
                    if dist.get(o, inf) == cost + w:
                        rev[o].add(i)
            return -1
        dijkstras(0, n-1)


        ans=[False]*len(edges)
        s = set()
        q=[n-1]
        while q:
            q2=[]
            for x in q:
                for i in rev[x]:
                    ans[i]=True
                    u,v,w=edges[i]
                    if x==u:
                        q2.append(v)
                    else:
                        q2.append(u)
            q=q2
        return ans