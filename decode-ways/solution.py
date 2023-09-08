class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        @cache
        def dfs(i):
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            ans=dfs(i+1)
            if i+1<n:
                x=int(s[i:i+2])
                if 1<=x and x<=26:
                    ans+=dfs(i+2)
            return ans
        return dfs(0)