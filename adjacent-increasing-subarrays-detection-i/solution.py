class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        i=0
        prev=0
        ans=0
        for j in range(n):
            if j!=0 and nums[j]<=nums[j-1]:
                i=j
                prev=cur
            cur=j-i+1
            if cur==k*2 or (cur==k and prev>=k):
                return True
        return False                