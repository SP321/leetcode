class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checksudoku(a,x,y,r,c):
            b=set()
            for i in range(x,x+c):
                for j in range(y,y+r):
                    if a[i][j]!='.' and a[i][j] in b:
                        return False
                    b.add(a[i][j])
            return True
        ans=True
        for i in range(0,9,3):
            for j in range(0,9,3):
                ans=ans and checksudoku(board,i,j,3,3)
        for i in range(9):
            ans=ans and checksudoku(board,i,0,9,1)
            ans=ans and checksudoku(board,0,i,1,9)
        return ans
                    