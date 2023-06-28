class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph=defaultdict(set)
        for (u,v),x in zip(edges,succProb):
            graph[u].add((v,x))
            graph[v].add((u,x))
        seen=set()
        probs = [0.0 for _ in range(n)]
        probs[start] = 1.0
        queue = [(-1.0, start)] 
        while queue:
            prob, node = heapq.heappop(queue)
            prob = -prob
            if prob < probs[node]:
                continue
            for neighbor, nprob in graph[node]:
                if prob * nprob > probs[neighbor]:
                    probs[neighbor] = prob * nprob
                    heapq.heappush(queue, (-probs[neighbor], neighbor))
        return probs[end]