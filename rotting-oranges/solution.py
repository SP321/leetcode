class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        ans=0
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
    
        enq=set()
        while q:
            ans+=1
            for _ in range(len(q)):
                x,y=q.popleft()
                for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if (xx,yy) not in enq:
                        if xx>=0 and xx<n and yy>=0 and yy<m and grid[xx][yy]==1:
                            enq.add((xx,yy))
                            grid[xx][yy]=2
                            q.append((xx,yy))


        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        
        return max(0,ans-1)