class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(dict)
        for u, v, w in edges:
            self.g[u][v] = w

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.g[u][v] = w
        

    def shortestPath(self, node1: int, node2: int) -> int:
        seen =  set()
        heap = [(0, node1)]
        while heap:
            cost, node = heappop(heap)
            if node == node2:
                return cost
            if node not in seen and node in self.g:
                seen.add(node)
                for kid, cost1 in self.g[node].items():
                    heappush(heap, (cost + cost1, kid))
        return -1