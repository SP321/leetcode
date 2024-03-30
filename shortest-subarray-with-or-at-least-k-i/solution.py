class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
      n=len(nums)
      ans=inf
      for i in range(n):
         for j in range(i+1,n+1):
            if list(accumulate(nums[i:j],lambda x,y:x|y))[-1]>=k:
               ans=min(ans,j-i)
      return ans if ans!=inf else -1
                