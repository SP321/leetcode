class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        list_s = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1:
                    list_s.extend([(i, j)] * max(0,grid[i][j]-1))
        
        list_f = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 0]


        def d(mapping) -> int:
            return sum([abs(s[0] - f[0]) + abs(s[1] - f[1]) for s, f in mapping])
        
        perms = itertools.permutations(list_f, len(list_s))

        ans = float('inf')
        for mapping in perms:
            distance = d(list(zip(list_s, mapping)))
            ans = min(ans, distance)
            
        return ans