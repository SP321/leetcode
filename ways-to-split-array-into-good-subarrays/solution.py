class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        x=[]
        for i in range(len(nums)):
            if nums[i]==1:
                x.append(i)
        if len(x)==0:
            return 0
        if len(x)==1:
            return 1
        ans=1
        for b in range(1,len(x)):
            a=b-1
            ans*=x[b]-x[a]
            ans%=10**9+7
        return ans