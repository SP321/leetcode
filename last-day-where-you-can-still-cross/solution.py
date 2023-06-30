class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        size = row * col
        uf = UnionFind(size + 2)
        s, t = size, size + 1
        grid = [-1 for _ in range(size + 2)]
        
        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            num = r * col + c
            grid[num] = num
            if r == 0:
                uf.union(num, s)
            if r == row - 1:
                uf.union(num, t)
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                nxt_num = rr * col + cc
                if 0 <= rr < row and 0 <= cc < col and grid[nxt_num] != -1:
                    uf.union(num, nxt_num)
                    if uf.find(s) == uf.find(t):
                        return i
        return -1
