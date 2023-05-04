from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        xs = []
        for x1, x2, h in buildings:
            xs.append((x1, -h))
            xs.append((x2, h))
        xs.sort()
        queue = [0]
        ans = []
        prev = 0
        for x, h in xs:
            if h<0:
                heappush(queue, h)
            else:
                queue.remove(-h)
                heapify(queue)
            cur = -queue[0]
            if cur != prev:
                ans.append([x, cur])
                prev = cur
        
        return ans