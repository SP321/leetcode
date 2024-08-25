MOD=10**9+7
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        if multiplier==1:
            return nums

        n=len(nums)
        h=[(x,i) for i,x in enumerate(nums)]
        heapify(h)
        mx=max(nums)

        while k and h[0][0]<=mx:
            x,i=heappop(h)
            nums[i]=x*multiplier
            heappush(h,(nums[i],i))
            k-=1


        full_cycles,rem=divmod(k,n)

        y=pow(multiplier,full_cycles,MOD)
        
        for _ in range(rem):
            x,i=heappop(h)
            nums[i]=x*multiplier

        return [(x*y)%MOD for x in nums]