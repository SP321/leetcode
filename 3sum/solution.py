class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        for k in range(len(nums)-1):
            if k>0 and nums[k]==nums[k-1]:
                continue
            i=k+1
            j=len(nums)-1
            while i<j:
                if nums[i]+nums[j]+nums[k]>0 :
                    j-=1
                elif nums[i]+nums[j]+nums[k]<0 :
                    i+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    j-=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
        return ans