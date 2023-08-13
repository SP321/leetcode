class Solution:
    def maxSum(self, nums: List[int]) -> int:
        x=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if max(str(nums[i]))==max(str(nums[j])):
                    x.append(nums[i]+nums[j])
        return max(x) if len(x)>0 else -1
                    
        