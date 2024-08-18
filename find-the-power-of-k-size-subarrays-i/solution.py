class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        i=0
        n=len(nums)
        ans=[-1]*(n-(k-1))
        for j in range(n):
            if j>0 and nums[j]-nums[j-1]!=1:
                i=j
            while j-i+1>=k:
                ans[i]=nums[i+k-1]
                i+=1
        return ans
                
        