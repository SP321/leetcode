class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
       	n, m = len(mat), len(mat[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = n * m
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            i, j = q.popleft()
            for x, y in dirs:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] > mat[i][j] + 1:
                    mat[ni][nj] = mat[i][j] + 1
                    q.append((ni, nj))
        return mat