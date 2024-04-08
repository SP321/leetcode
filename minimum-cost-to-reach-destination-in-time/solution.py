class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        g = defaultdict(list)
        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))

        h = [(passingFees[0],0,0)]
        dist = {0: 0}
        while h:
            cost,time,cur = heappop(h)
            if cur == n-1:
                return cost
            for o, t in g[cur]:
                if dist.get(o, inf) > time+t and time+t<=maxTime:
                    dist[o] = time+t
                    heappush(h, (cost + passingFees[o], time+t,o))
        return -1