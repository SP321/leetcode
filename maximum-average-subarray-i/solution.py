class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=-inf
        c=0
        i=0
        for j in range(len(nums)):
            c+=nums[j]
            if j-i+1>k:
                c-=nums[i]
                i+=1
            if j+1>=k:
                ans=max(ans,c)
        return ans/k