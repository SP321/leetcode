class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)
        c=[0]*(1<<17)
        ans=0
        for mask in range(1<<n):
            cur=0
            for i in range(n):
                if mask>>i&1:
                    cur|=nums[i]
            c[cur]+=1
            if c[cur]>ans:
                ans=c[cur]
        return ans