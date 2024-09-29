class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])

        for x in range(n):
            for y in range(m):
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<n and 0<=ny<m:
                        board[nx][ny]+=(board[x][y]&1)<<1

        for i in range(n):
            for j in range(m):
                if board[i][j]&1:
                    if 2<=board[i][j]>>1<=3:
                        board[i][j]=1
                    else:
                        board[i][j]=0
                elif board[i][j]>>1==3:
                    board[i][j]=1
                else:
                    board[i][j]=0
