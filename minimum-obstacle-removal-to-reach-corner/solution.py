class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque([(0,(0,0))])
        dist=[[inf]*m for _ in range(n)]
        dist[0][0]=0
        while q:
            d,node=q.popleft()
            if dist[node[0]][node[1]]!=d:
                continue
            if node==(n-1,m-1):
                return d
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                x=node[0]+dx
                y=node[1]+dy
                if 0<=x<n and 0<=y<m:
                    o=(x,y)
                    if dist[x][y]>d+grid[x][y]:
                        if grid[x][y]:
                            dist[x][y]=d+1
                            q.append((d+1,o))
                        else:
                            dist[x][y]=d
                            q.appendleft((d,o))
        return -1