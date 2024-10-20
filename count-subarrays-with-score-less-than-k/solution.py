class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        sc=0
        i=0
        for j in range(n):
            sc+=nums[j]
            while sc*(j-i+1)>=k:
                sc-=nums[i]
                i+=1
            ans+=(j-i+1)
        return ans
