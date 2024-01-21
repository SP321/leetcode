class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = float('inf')

        for i in range(n):
            for j in range(i+1,n):
                dist[i][j]=j-i
                dist[j][i]=j-i
        x-=1
        y-=1
        dist[x][y]=1
        dist[y][x]=1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        ans=[0]*n
        
        for i in range(n):
            for j in range(n):
                if i!=j and dist[i][j] not in [0,float('inf')]:
                    ans[dist[i][j]-1]+=1
        return ans