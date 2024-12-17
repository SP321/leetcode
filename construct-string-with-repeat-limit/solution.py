class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        pq = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(pq)
        
        ans = []
        while pq:
            ch, count = heapq.heappop(pq)
            ch = chr(-ch)
            used = min(repeatLimit, count)
            ans.append(ch * used)
            count -= used
            
            if count > 0:
                if not pq: break
                next_ch, next_count = heapq.heappop(pq)
                ans.append(chr(-next_ch))
                next_count -= 1
                
                if next_count > 0:
                    heapq.heappush(pq, (next_ch, next_count))
                heapq.heappush(pq, (-ord(ch), count))
        
        return "".join(ans)