def manacher_odd(s):
    n = len(s)
    s =["$"] + s + ["^"]
    p = [0] * (n + 2)
    l, r = 1, 1
    for i in range(1, n + 1):
        p[i] = max(0, min(r - i, p[l + (r - i)]))
        while s[i - p[i]] == s[i + p[i]]:
            p[i] += 1
        if i + p[i] > r:
            l,r = i - p[i], i + p[i]
    return p[1:-1]

def manacher(s):
    t = []
    for c in s:
        t.append("#")
        t.append(c)
    t.append("#")
    res = manacher_odd(t)
    return res[1:-1]

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n=len(parent)
        g=defaultdict(list)
        for v,u in enumerate(parent):
            g[u].append(v)
        for i in range(n):
            g[i]=sorted(g[i])
        start=[0]*n
        end=[0]*n
        a=[]
        def dfs(u):
            start[u]=len(a)
            for v in g[u]:
                dfs(v)
            a.append(s[u])
            end[u]=len(a)
        dfs(0)
        mn=manacher(a)
        ans=[False]*n
        for node in range(n):
            sz=(end[node]-start[node])
            mid=start[node]+sz//2
            if sz%2==0:
                mpos=mid*2-1
            else:
                mpos=mid*2

            ans[node]=mn[mpos]>=sz
        return ans