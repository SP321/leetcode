class Solution:
    def findMin(self, nums: List[int]) -> int:
        x=nums[0]
        i=0
        j=len(nums)-1
        ans=i
        while i<=j:
            m=i+(j-i)//2
            if nums[m]>=x:
                i=m+1
            else:
                ans=m
                j=m-1
        return nums[ans]
            