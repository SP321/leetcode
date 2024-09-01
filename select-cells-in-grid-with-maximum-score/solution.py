class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        g=defaultdict(list)
        for i,row in enumerate(grid):
            for x in row:
                g[x].append(i)
        n=len(g)
        dp0=defaultdict(int)
        dp0[0]=0
        for x,a in g.items():
            dp1=defaultdict(int)
            for i in a:
                for y,c in dp0.items():
                    if (1<<i)&y==0:
                        dp1[(1<<i)|y]=max(dp1[(1<<i)|y],c+x)
            for x,v in dp1.items():
                dp0[x]=max(dp0[x],v)
        return max(dp0.values())
