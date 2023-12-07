class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      d=defaultdict(set)
      for i in range(9):
        for j in range(9):
          x=board[i][j]
          if x=='.':
            continue
          row="r"+str(i)
          col="c"+str(j)
          grid="g"+str(i//3)+str(j//3)
          for key in [row,col,grid]:
            if x in d[key]:
              return False
            d[key].add(x)
      return True
      