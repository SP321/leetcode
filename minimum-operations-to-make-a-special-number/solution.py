class Solution:
    def minimumOperations(self, num: str) -> int:
        selects=["00","52","05","57"]
        x=num[::-1]
        def check(a,b):
            @cache
            def dp(i,j):
                if j==len(b):
                    return 0
                if i==len(a):
                    return 100
                if a[i]==b[j]:
                    return dp(i+1,j+1)
                return dp(i+1,j)+1
            return min( dp(0,0) , len(a)-a.count('0') )
        ans=len(num)
        for i in selects:
            deletions=check(x,i)
            ans=min(ans,deletions)
        return ans
            
            
        