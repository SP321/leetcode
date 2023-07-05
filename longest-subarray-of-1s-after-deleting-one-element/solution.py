class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c=0
        l=0
        ans=0
        for r in range(len(nums)):
            if nums[r]!=1:
                c+=1
            if c==2:
                while nums[l]==1:
                    l+=1
                l+=1
                c-=1
            else:
                ans=max(ans,r-l)
        return ans
            
