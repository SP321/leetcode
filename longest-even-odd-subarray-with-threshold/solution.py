class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        x=[1 if i%2==0 and i<=threshold else 0 for i in nums]
        for i in range(1,len(nums)):
            if nums[i]%2!=nums[i-1]%2 and nums[i]<=threshold and nums[i-1]<=threshold:
                x[i]=max(x[i],1+x[i-1])
        return max(x)