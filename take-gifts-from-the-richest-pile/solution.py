class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h=[-x for x in gifts]
        heapify(h)
        for _ in range(k):
            x=heappop(h)
            heappush(h,-int(sqrt(-x)))
        return -sum(h)