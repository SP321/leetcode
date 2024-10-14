class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h=[]
        for x in nums:
            heappush(h,-x)
        ans=0
        for _ in range(k):
            cur=-heappop(h)
            ans+=cur
            heappush(h,-math.ceil(cur/3))
        return ans