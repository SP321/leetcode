class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        i=0
        ans=0
        c=Counter()
        for j in range(len(nums)):
            c[nums[j]]+=1
            while c[mx]>=k:
                c[nums[i]]-=1
                i+=1
            ans+=i
        return ans