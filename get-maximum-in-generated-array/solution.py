class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        x=[0]*(n+1)
        x[1]=1
        ans=1
        for i in range(1,n):
            if 2*i<=n:
                x[2*i]=x[i]
            if i>1 and 2*(i-1)+1<=n:
                x[2*(i-1)+1]=x[i]+x[i-1]
                ans=max(ans,x[2*(i-1)+1])
        return ans