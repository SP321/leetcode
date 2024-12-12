class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h=[]
        for x in gifts:
            heappush(h,-x)
        for _ in range(k):
            cur=-heappop(h)
            heappush(h,-(int(sqrt(cur))))
        return -sum(h)