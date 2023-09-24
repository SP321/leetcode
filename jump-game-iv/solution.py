
class Solution:
    def minJumps(self, arr: list[int]) -> int:
        c = defaultdict(list)
        n = len(arr)
        for i in range(n):
            c[arr[i]].append(i)
        
        visited = set()
        pq = deque([(0, 0)])
        while pq:
            i, steps = pq.popleft()
            
            if i == n - 1:
                return steps

            visited.add(i)
            
            if i + 1 < n and i + 1 not in visited:
                pq.append((i + 1, steps + 1))
                
            if i - 1 >= 0 and i - 1 not in visited:
                pq.append((i - 1, steps + 1))
                
            for j in c[arr[i]]:
                if j not in visited:
                    pq.append((j, steps + 1))
                    
            del c[arr[i]]
        
        return -1