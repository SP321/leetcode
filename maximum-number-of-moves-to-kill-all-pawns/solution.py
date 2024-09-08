moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
@cache
def get_mat(x,y):
    d = [[-1] * 50 for _ in range(50)]
    d[x][y] = 0
    q = deque([(x, y)])
    c = 0
    while q:
        c += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in moves:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < 50 and 0 <= yy < 50 and d[xx][yy] == -1:
                    d[xx][yy] = c
                    q.append((xx, yy))
    return d

# for i in range(50):
#     for j in range(50):
#         get_mat(i,j)

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        n = len(positions)

        @cache
        def dp(alice,x,y,mask=0):
            if mask.bit_count()==n:
                return 0
            d=get_mat(x,y)
            ans=-inf if alice else inf
            for i,(px,py) in enumerate(positions):
                if mask & (1 << i) == 0:
                    moves = d[px][py] + dp(not alice, px, py, mask | (1 << i))
                    if alice:
                        ans = max(ans, moves)
                    else:
                        ans = min(ans,moves)
            return ans
        return dp(True, kx, ky)