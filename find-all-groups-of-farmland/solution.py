class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        n = len(land)
        m = len(land[0])
        ans = []

        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    x=i
                    while x < n and land[x][j] == 1:
                        y = j
                        while y < m and land[x][y] == 1:
                            land[x][y] = 0
                            y += 1
                        x += 1
                    ans.append([i, j, x - 1, y - 1])
        
        return ans