class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.parent = parent
        self.bin_max = int(math.log2(n) + 1)

        self.up = [[-1] * self.bin_max for _ in range(n)]
        
        for i in range(n):
            self.up[i][0] = parent[i]
        
        for j in range(1, self.bin_max):
            for i in range(n):
                if self.up[i][j-1] != -1:
                    self.up[i][j] = self.up[self.up[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.bin_max):
            if k & (1 << j):
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)