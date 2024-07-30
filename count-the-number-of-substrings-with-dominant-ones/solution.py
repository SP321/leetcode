def triangle(n): return (n*(n+1))//2 if n>=0 else 0
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        z=[-1]+[i for i,x in enumerate(s) if x=='0']+[n]
        ans=0
        for x,y in pairwise(z):
            ans+=triangle(y-x-1)
        max_zeros=int(sqrt(n-(len(z)-2 ) ))+1
        for zero_c in range(1,max_zeros):
            for i in range(1, len(z) - zero_c):
                j = i + zero_c - 1
                l = z[i] - z[i-1]
                r = z[j+1] - z[j]
                min_ones=zero_c**2
                window_sz=z[j]-z[i]+1
                have_ones=window_sz-zero_c
                take = min_ones-have_ones
                if take < l + r:
                    ans += l * r
                    ans -= triangle(take)
                    ans += triangle(take - l)
                    ans += triangle(take - r)
        return ans