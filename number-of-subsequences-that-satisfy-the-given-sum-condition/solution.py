class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        ans=0
        while True:
            while  i<j and nums[i]+nums[j] >target:
                j-=1
            if i>j or nums[i]+nums[j] >target:
                break
            ans+=2**(j-i)
            ans%=int(1e9+7)
            i+=1
        return ans

        