class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g=defaultdict(list)
        for u, v, p in flights:
            g[u].append((v, p))
        
        q = deque()
        q.append((0,src))

        dists = [float('inf') for _ in range(n)]
        dists[src] = 0

        for _ in range(k+1):
            if not q:
                break
            q2=[]
            for dist,u in q:
                for v, w in g[u]:
                    if dists[v] > dist + w:
                        dists[v] = dist + w
                        q2.append((dists[v], v))
            q=q2
        
        return -1 if dists[dst] == float('inf') else dists[dst]