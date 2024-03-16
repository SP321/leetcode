class Solution:
    def minimizeStringValue(self, s: str) -> str:
        c=Counter(s)
        h=[(c[x],x) for x in ascii_lowercase]
        heapq.heapify(h)
        a=[]
        for _ in range(c['?']):
            c,y=heapq.heappop(h)
            heapq.heappush(h,(c+1,y))
            a.append(y)
        a.sort(reverse=True) #reverse sort for cheaper pop operations
        ans=[]
        for x in s:
            if x=='?':
                ans.append(a.pop())
            else:
                ans.append(x)
        return ''.join(ans)