class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        c=Counter()
        sm=0
        i=0
        ans=0
        for j in range(len(nums)):
            c[nums[j]]+=1
            sm+=nums[j]
            while j-i+1>k or c[nums[j]]>1:
                sm-=nums[i]
                c[nums[i]]-=1
                i+=1
            if j-i+1==k:
                ans=max(ans,sm)
        return ans