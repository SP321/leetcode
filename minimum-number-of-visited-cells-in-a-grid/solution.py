from sortedcontainers import SortedList
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        sright= [SortedList(range(m)) for _ in range(n)]
        sdown = [SortedList(range(n)) for _ in range(m)]
        q = deque([(0, 0, 1)])

        while q:
            i, j, d = q.popleft()
            if (i, j) == (n-1, m-1):
                return d
            for k in list(sright[i].irange(j+1, min(j+1+grid[i][j], m) - 1)):
                q.append((i, k, d+1))
                sright[i].remove(k)
                sdown[k].remove(i)
            for k in list(sdown[j].irange(i+1, min(i+1+grid[i][j], n) - 1)):
                q.append((k, j, d+1))
                sdown[j].remove(k)
                sright[k].remove(j)
        return -1