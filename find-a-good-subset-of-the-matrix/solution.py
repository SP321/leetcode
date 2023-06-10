class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        s = set()
        ind={}
        for i in range(n):
            x = 0
            for j in grid[i]:
                x = (x << 1) | j
            s.add((x))
            ind[x]=i
        gr = list(s)
        n = len(gr)
        for i in range(n):
            x=gr[i]
            if x == 0:
                return [ind[x]]
        for i in range(n):
            x=gr[i]
            for j in range(i + 1, n):
                y=gr[j]
                if x&y == 0:
                    return sorted([ind[x], ind[y]])
        return []