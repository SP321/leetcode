class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        m=n//2
        ans=abs(k-nums[m])
        for i in range(m+1,n):
            if nums[i]>=k:
                break
            ans+=k-nums[i]
        for i in range(m-1,-1,-1):
            if nums[i]<=k:
                break
            ans+=nums[i]-k
        return ans