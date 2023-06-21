class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        left,right=1,10**6
        ans=float('inf')
        while left<=right:
            mid=left+(right-left)//2
            c1,c2=0,0
            for i in range(len(nums)):
                c1+=abs(nums[i]-mid)*cost[i]
                c2+=abs(nums[i]-(mid+1))*cost[i]
            if c1<c2:
                right=mid-1
            else:
                left=mid+1
            ans=min(ans,c1,c2)
        return ans