class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ans=nums[0]
        for i,x in enumerate(nums):
            if i>0:
                if x==nums[i-1]+1:
                    ans+=x
                else:
                    break
        for x in sorted(nums):
            if x==ans:
                ans+=1
        return ans