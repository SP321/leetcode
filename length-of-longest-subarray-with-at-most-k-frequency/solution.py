class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i=0
        c=Counter()
        ans=0
        for j in range(len(nums)):
            c[nums[j]]+=1
            while i<j and c[nums[j]]>k:
                c[nums[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans
                