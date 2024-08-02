class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        c=nums.count(1)
        n=len(nums)
        i=0
        cur=0
        ans=c
        for j in range(n*2):
            cur+=nums[j%n]
            while j-i+1>c:
                cur-=nums[i%n]
                i+=1
            if j-i+1==c:
                ans=min(ans,c-cur)
        return ans

                

