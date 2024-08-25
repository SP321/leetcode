class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n=len(nums)
        h=[(x,i) for i,x in enumerate(nums)]
        heapify(h)
        for _ in range(k):
            x,i=heappop(h)
            nums[i]*=multiplier
            heappush(h,(nums[i],i))
        return nums