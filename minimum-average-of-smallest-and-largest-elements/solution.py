class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans=inf
        i=0
        j=len(nums)-1
        while i<j:
            ans=min(ans,(nums[j]+nums[i])/2)
            i+=1
            j-=1
        return ans