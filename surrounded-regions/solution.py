class Solution:
    def solve(self, board: List[List[str]]) -> None:
        b2=copy.deepcopy(board)
        def dfs(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return
            if b2[x][y]=="X":
                return
            b2[x][y]="X"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        n=len(b2)
        m=len(b2[0])
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)
        for j in range(m):
            dfs(0,j)
            dfs(n-1,j)
        print(board,b2)
        def dfs2(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return
            if b2[x][y]=="X":
                return
            b2[x][y]="X"
            board[x][y]="X"
            dfs2(x+1,y)
            dfs2(x-1,y)
            dfs2(x,y+1)
            dfs2(x,y-1)
        for i in range(n):
            for j in range(m):
                if b2[i][j]=='O':
                    dfs2(i,j)
