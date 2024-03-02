class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h=nums
        heapq.heapify(h)
        c=0
        while h:
            a=heapq.heappop(h)
            if a>=k:
                return c
            c+=1
            b=heapq.heappop(h)
            heapq.heappush(h,min(a,b)*2+max(a,b))
        return -1