class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=0
        p=1
        ans=0
        for j in range(n):
            p*=nums[j]
            while i<j and p>=k:
                p//=nums[i]
                i+=1
            if p<k:
                ans+=j-i+1
        return ans
