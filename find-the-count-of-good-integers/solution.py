class Solution:
    @cache
    def countGoodIntegers(self, n: int, k: int) -> int:
        half=(n+1)//2
        def comb_r(n, r):
            return math.comb(n + r - 1, r)
        def get_count(freq):
            nz=sum(freq[1:])
            numerator = factorial(nz)
            denominator = 1
            for v in freq[1:]:
                denominator*=factorial(v)
            ways = numerator*comb_r(nz,freq[0])//denominator
            return ways
        seen=set()
        cur_num=[None]*n
        ans=0
        for i in range(10**(half-1),10**half):
            arr=str(i)
            r=0
            for i,x in enumerate(arr):
                idx={i,n-i-1}
                for y in idx:
                    cur_num[y]=x
                    r+=(10**y)%k * int(x)
                    r%=k
            if r==0:
                c=Counter(cur_num)
                x=tuple(c[str(i)] for i in range(10))
                if x not in seen:
                    seen.add(x)
                    ans+=get_count(x)
        return ans