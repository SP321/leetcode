class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n=len(grid)
        g=defaultdict(list)
        def connect(n1,n2):
            g[n1].append(n2)
            g[n2].append(n1)
        for i in range(n):
            for j in range(n):
                if(j>0):
                    connect((i,j-1,'r'),(i,j,'l'))
                if(i>0):
                    connect((i-1,j,'b'),(i,j,'t'))
                if grid[i][j]=='\\':
                    connect((i,j,'l'),(i,j,'b'))
                    connect((i,j,'t'),(i,j,'r'))
                elif grid[i][j]=='/':
                    connect((i,j,'l'),(i,j,'t'))
                    connect((i,j,'b'),(i,j,'r'))
                else:
                    connect((i,j,'l'),(i,j,'b'))
                    connect((i,j,'l'),(i,j,'t'))
                    connect((i,j,'t'),(i,j,'r'))
                    connect((i,j,'b'),(i,j,'r'))

        visited=set()
        def dfs(x):
            for y in g[x]:
                if y not in visited:
                    visited.add(y)
                    dfs(y)
        ans=0
        for x in g:
            if x not in visited:
                dfs(x)
                ans+=1
        return ans
