class Solution:
    def restoreMatrix(self, a: List[int], b: List[int]) -> List[List[int]]:
        n=len(a)
        m=len(b)
        ans=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j]=min(a[i],b[j])
                a[i]-=ans[i][j]
                b[j]-=ans[i][j]
        return ans