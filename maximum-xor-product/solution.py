class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        for i in range(n):
            if (a>>i)&1==0 and (b>>i)&1 ==0:
                a|=1<<i
                b|=1<<i
        for i in range(n)[::-1]:
            if (a>>i)&1 != (b>>i)&1:
                aa,bb= a^(1<<i),b^(1<<i)
                if aa*bb > a*b:
                    a,b=aa,bb
        ans=a*b
        return ans%(10**9+7)