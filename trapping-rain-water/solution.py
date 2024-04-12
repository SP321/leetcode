class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lmax=list(accumulate(height,max))
        rmax=list(accumulate(height[::-1],max))[::-1]
        return sum(min(lmax[i],rmax[i])-height[i] for i in range(1,n-1))