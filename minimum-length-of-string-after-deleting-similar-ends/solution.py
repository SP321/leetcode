class Solution:
    def minimumLength(self, s: str) -> int:
        d=deque(x for x in s)
        ans=len(s)
        while len(d)>1:
            x=d[0]
            if x!=d[-1]:
                break
            while d and d[0]==x:
                d.popleft()
            while d and d[-1]==x:
                d.pop()
            ans=len(d)
        return ans
            
