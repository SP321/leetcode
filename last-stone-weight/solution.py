class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a=[-i for i in stones]
        heapq.heapify(a)
        while len(a)>1:
            x,y=heapq.heappop(a),heapq.heappop(a)
            if x!=y:
                y=x-y
                heapq.heappush(a,y)
        return -a[0] if len(a)>0 else 0

