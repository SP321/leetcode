class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        nums.append(-inf)
        n=len(nums)
        i=0
        prev=0
        ans=0
        for j in range(n):
            if j!=0 and nums[j]<=nums[j-1]:
                cur=j-i
                i=j
                ans=max(ans,cur//2)
                ans=max(ans,min(prev,cur))
                prev=cur
        return ans