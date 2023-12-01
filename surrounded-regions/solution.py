class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return
            if board[x][y]=="X" or board[x][y]=='.':
                return
            board[x][y]="."
            for xx,yy in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
                dfs(xx,yy)
        n=len(board)
        m=len(board[0])
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)
        for j in range(m):
            dfs(0,j)
            dfs(n-1,j)

        for i in range(n):
            for j in range(m):
                if board[i][j]=='.':
                    board[i][j]="O"
                else:
                    board[i][j]="X"
                    