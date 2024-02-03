class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pref=list(accumulate(nums,initial=0))
        d={}
        ans=float('-inf')
        for i,x in enumerate(nums):
            if x not in d:
                d[x]=i
            elif pref[i]<pref[d[x]]:
                d[x]=i
            target=[x-k,x+k]
            for t in target:
                if t in d:
                    ans=max(ans,pref[i+1]-pref[d[t]])
        return ans if ans!=float("-inf") else 0