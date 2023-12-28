class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        s=0
        i=0
        ans=float('inf')
        for j in range(n):
            s+=nums[j]
            while s>=target:
                ans=min(ans,j-i+1)
                s-=nums[i]
                i+=1
        return ans if ans!=float("inf") else 0