class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary=set(dictionary)
        n = len(s)
        @cache
        def dp(i):
            if i==n:
                return 0
            ans=float('inf')
            for j in range(i+1,n+1):
                if s[i:j] in dictionary:
                    ans=min(ans,dp(j))
                else:
                    ans=min(ans,dp(j)+j-i)
            return ans
        return dp(0)