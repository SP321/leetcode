class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        N = len(s)
        INF = 10 ** 20
        orda = ord('a')

        nxt = collections.defaultdict(list)
        
        for start in range(N):
            f = collections.Counter()
            mx = 0
            total = 0
            for end in range(start, N):
                c = ord(s[end]) - orda
                f[c] += 1
                
                if f[c] > mx:
                    mx = f[c]
                total += 1
                
                if mx * len(f) == total:
                    nxt[start].append(end)
        
        @cache
        def go(index):
            if index == N:
                return 0
            
            best = INF
            for nindex in nxt[index]:
                best = min(best, go(nindex + 1) + 1)
            return best
        
        return go(0)