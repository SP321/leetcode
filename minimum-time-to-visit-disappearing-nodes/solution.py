class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
            g=defaultdict(list)
            for u,v,w in edges:
                g[u].append((v,w))
                g[v].append((u,w))
            h = [(0,0)]
            dist = {0: 0}
            while h:
                cost, cur = heapq.heappop(h)
                if dist[cur] != cost:
                    continue
                for o, w in g[cur]:
                    if dist.get(o, inf) > cost + w and cost+w<disappear[o]:
                        dist[o] = cost + w
                        heapq.heappush(h, (cost + w, o))
            return [dist.get(i,-1) for i in range(n)]