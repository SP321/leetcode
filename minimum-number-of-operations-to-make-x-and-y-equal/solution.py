class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        def moves(a):
            ans=[a+1,a-1]
            if a%11==0:
                ans.append(a//11)
            if a%5==0:
                ans.append(a//5)
            return ans
                
        def dijkstras_10(start):
            h = deque([(0,start)])
            dist = {start: 0}

            while h:
                cost, cur = h.popleft()
                if cur==y:
                    return cost
                for val in moves(cur):
                    if val not in dist or dist[val] > cost + 1:
                        dist[val] = cost+1
                        h.append((cost+1,val))
            return dist
      
        return dijkstras_10(x)