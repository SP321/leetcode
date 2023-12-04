class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans=[[0]*n for i in range(n)]
        for x1,y1,x2,y2 in queries:
            for i in range(x1,x2+1):
                ans[i][y1]+=1
                if y2<n-1:
                    ans[i][y2+1]-=1
        for i in range(n):
            cur=0
            for j in range(n):
                cur+=ans[i][j]
                ans[i][j]=cur
        return ans
