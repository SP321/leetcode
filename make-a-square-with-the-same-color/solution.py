class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                if max(Counter(grid[i][j]+grid[i+1][j]+ grid[i][j+1]+ grid[i+1][j+1]).values())>=3:
                    return True
        return False