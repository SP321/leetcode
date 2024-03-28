class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        c=Counter()
        i=0
        ans=0
        for j in range(len(nums)):
            c[nums[j]]+=1
            while c[nums[j]]>k:
                c[nums[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans