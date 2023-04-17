class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        x=height[0]
        lmax=[x]*n
        for i,a in enumerate(height):
            x=max(x,a)
            lmax[i]=x
        x=height[n-1]
        rmax=[x]*n
        for i,a in list(enumerate(height))[::-1]:
            x=max(x,a)
            rmax[i]=x
        ans=0
        i=1
        while i<n-1:
            wallheight=min(lmax[i],rmax[i])
            while height[i]<wallheight:
                ans+=wallheight-height[i]
                i+=1
            i+=1
        return ans
                

