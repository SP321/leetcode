class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h=[-x for x in nums]
        heapify(h)
        ans=0
        for _ in range(k):
            x=-heappop(h)
            ans+=x
            heappush(h,- math.ceil(x/3))
        return ans