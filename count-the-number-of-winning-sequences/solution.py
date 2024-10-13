class Solution:
    def countWinningSequences(self, s: str) -> int:
        opts="FWE"
        @cache
        def score(x,y):
            if x==y:
                return 0
            if x=='F' and y=='E':
                return 1
            if x=='W' and y=='F':
                return 1
            if x=='E' and y=='W':
                return 1
            return -1
            
        dp0=[
             Counter([score(opts[0],s[0])]),
             Counter([score(opts[1],s[0])]),
             Counter([score(opts[2],s[0])])
        ]

        for x in s[1:]:
            dp1=[Counter(),Counter(),Counter()]
            for sc,v in dp0[0].items():
                dp1[1][sc+score(opts[1],x)]+=v
                dp1[2][sc+score(opts[2],x)]+=v
            for sc,v in dp0[1].items():
                dp1[0][sc+score(opts[0],x)]+=v
                dp1[2][sc+score(opts[2],x)]+=v
            for sc,v in dp0[2].items():
                dp1[0][sc+score(opts[0],x)]+=v
                dp1[1][sc+score(opts[1],x)]+=v
            dp0=dp1

        ans=0
        for c in dp0:
            for x,v in c.items():
                if x>0:
                    ans+=v
                    ans%=(10**9+7)
        return ans