class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        keyCount = 0
        start = (0,0,'')
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start = (i,j,'')
                elif grid[i][j].islower():
                    keyCount += 1
        q = deque()
        q.append(start)
        visited = set()
        def add_to_queue(i,j,keyStr):
            for r,c in [[i,j-1],[i,j+1],[i-1,j],[i+1,j]]:
                if r<0 or c<0 or r>=n or c>=m:
                    continue
                q.append((r,c,keyStr))
        steps = 0
        while q:
            level = []
            while q:
                level.append(q.popleft())
            for state in level:
                i,j,keyStr = state
                if (i,j,keyStr) in visited or grid[i][j] == '#':
                    continue
                c = grid[i][j]
                if c.isupper():
                    if c.lower() not in keyStr:
                        continue
                    else:
                        add_to_queue(i,j,keyStr)
                elif c.islower():
                    if c not in keyStr:
                        keyStr += c
                        if len(keyStr) == keyCount:
                            return steps
                        add_to_queue(i,j,keyStr)
                    else:
                        add_to_queue(i,j,keyStr)
                else:
                    add_to_queue(i,j,keyStr)
                visited.add((i,j,keyStr))
            steps += 1    
        return -1