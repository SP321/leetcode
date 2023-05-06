class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x=nums[0]
        i=0
        j=len(nums)-1
        while i<=j:
            m=i+(j-i)//2
            if target==nums[m]:
                return m
            if nums[m]<x:
                if(target<nums[m] or target >=x):
                    j=m-1
                else:
                    i=m+1
            else:
                if target<nums[m] and target >=x:
                    j=m-1
                else:
                    i=m+1
        return -1