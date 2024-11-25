moves = [ 
    [1,3],
    [0,2,4],
    [1,5],
    [0,4],
    [3,1,5],
    [4,2]
]
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start=tuple((board[0]+board[1]))
        for i in range(6):
            if start[i]==0:
                start=i,start
                break
        q = deque([(start, 0)])
        dist = {start: 0}
        while q:
            cur, cost = q.popleft()
            if dist[cur] != cost:
                continue
            if cur[1] == (1,2,3,4,5,0):
                return cost
            state=list(cur[1])
            x=cur[0]
            for y in moves[x]:
                state[x],state[y]=state[y],state[x]
                o=(y,tuple(state))
                w=1
                if o not in dist or dist[o] > cost + w:
                    dist[o] = cost + w
                    q.append((o, dist[o]))
                state[x],state[y]=state[y],state[x]
        return -1