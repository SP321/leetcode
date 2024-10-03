class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        diff=sum(nums)%p
        if diff==0:
            return 0
        d={}
        d[0]=-1
        ans=inf
        cur=0
        n=len(nums)
        for i,x in enumerate(nums):
            cur+=x
            cur%=p
            y=(cur-diff)%p
            if y in d:
                ans=min(ans,i-d[y])
            d[cur]=i
        return ans if ans<n else -1
                