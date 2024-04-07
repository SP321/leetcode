class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        @cache
        def dp(i,c):
            if i==n:
                return c==0
            if s[i]=='(':
                ans=dp(i+1,c+1)
            elif s[i]==')':
                if c>0:
                    ans=dp(i+1,c-1)
                else:
                    return False
            else:
                ans=dp(i+1,c) or dp(i+1,c+1)
                if c>0:
                    ans |=dp(i+1,c-1)
            return ans
        return dp(0,0)
