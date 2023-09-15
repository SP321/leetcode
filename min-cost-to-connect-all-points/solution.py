class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        mst_set = set()
        mst_set.add(0)
        pq = [(dist(0, i), i) for i in range(1, n)]
        heapq.heapify(pq)

        ans = 0
        while len(mst_set) < n:
            distance, vertex = heapq.heappop(pq)
            if vertex not in mst_set:
                mst_set.add(vertex)
                ans += distance
                for i in range(n):
                    if i not in mst_set:
                        heapq.heappush(pq, (dist(vertex, i), i))
                        
        return ans