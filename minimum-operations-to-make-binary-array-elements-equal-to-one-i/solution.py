class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                ans+=1
                for j in range(i,i+3):
                    nums[j]^=1
        if sum(nums)==len(nums):
            return ans
        return -1