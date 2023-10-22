class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        @cache
        def changes(l, r):
            ans = inf
            length = r - l + 1
            factor = 1
            while factor * factor <= length:
                if length % factor == 0:
                    for m in {factor, length // factor}:
                        if m == length:
                            continue
                        ss = [''] * m
                        for i in range(l, r+1):
                            ss[i % m] += s[i]
                        ret = 0
                        for x in ss:
                            if len(x) % 2:
                                st = len(x) // 2
                                for j in range(st+1):
                                    if x[st-j] != x[st+j]:
                                        ret += 1
                            else:
                                st = len(x) // 2 - 1
                                for j in range(st+1):
                                    if x[st-j] != x[st+j+1]:
                                        ret += 1
                        ans = min(ans, ret)
                factor += 1
            return ans

        @cache
        def dp(i, k):
            if k < 0:
                return inf
            if i == n:
                return 0 if k == 0 else float('inf')
            ans = float('inf')
            for j in range(i+1, n):
                ans = min(ans, changes(i, j) + dp(j+1, k-1))
            return ans

        return dp(0, k)