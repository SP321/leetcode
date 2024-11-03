class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n=len(moveTime)
        m=len(moveTime[0])
        start=(0,0)
        end=(n-1,m-1)
        h = [(0,start)]
        dist = {start: 0}
        while h:
            cost, cur = heapq.heappop(h)
            if dist[cur] != cost:
                continue
            if cur == end:
                return cost
            x,y=cur
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                xx=x+dx
                yy=y+dy
                if 0<=xx<n and 0<=yy<m:
                    o=(xx,yy)
                    w=max(0,moveTime[xx][yy]-cost)+1
                    if dist.get(o, inf) > cost + w:
                        dist[o] = cost + w
                        heapq.heappush(h, (cost + w, o))