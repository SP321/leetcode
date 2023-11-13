class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.x=heapq.nlargest(k,nums)
        heapq.heapify(self.x)
        self.k=k

    def add(self, val: int) -> int:
        if len(self.x)!=self.k:
            heapq.heappush(self.x,val)
        elif val>self.x[0]:
            heapq.heappop(self.x)
            heapq.heappush(self.x,val)
        return self.x[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)