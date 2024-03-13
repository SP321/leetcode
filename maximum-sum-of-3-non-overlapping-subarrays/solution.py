class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        pre=list(accumulate(nums,initial=0))
        a = [pre[i+k] - pre[i] for i in range(n - k + 1)]
        left_max=[(x,-i) for i,x in enumerate(a)]
        right_max=[(x,-i) for i,x in enumerate(a)]
        n=len(a)
        for i in range(1,n):
            left_max[i]=max(left_max[i],left_max[i-1])
        for i in range(n-2,-1,-1):
            right_max[i]=max(right_max[i],right_max[i+1])
    
        ans=None
        best=-inf
        for i in range(k,len(a)-k):
            lx,li=left_max[i-k]
            rx,ri=right_max[i+k]
            cur=lx+a[i]+rx
            if cur>best:
                best=cur
                ans=[-li,i,-ri]
        return ans