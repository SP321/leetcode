class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        prev=None
        ans=0
        for j in range(n):
            if prev==nums[j]:
                ans+=1
                i=j
            else:
                ans+=j-i+1
            prev=nums[j]
        return ans