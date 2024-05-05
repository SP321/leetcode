def get_factors(n):
    ans=[]
    i=1
    while i*i<=n:
        if n%i==0:
            ans.append(i)
            if i*i!=n:
                ans.append(n//i)
        i+=1
    return sorted(ans)

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n=len(s)
        def check(k):
            c=Counter(s[:k])
            for i in range(1,n//k):
                c2=Counter(s[i*k:i*k+k])
                if c2!=c:
                    return False
            return True
        
        
        for factor in get_factors(n):
            if check(factor):
                return factor