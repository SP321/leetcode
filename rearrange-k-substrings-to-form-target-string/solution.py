class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n=len(s)
        sz=n//k
        s1=[]
        s2=[]
        a=[]
        b=[]
        for i in range(n+1):
            if i%sz==0:
                s1.append(''.join(a))
                s2.append(''.join(b))
                a=[]
                b=[]
            if i==n:
                break
            a.append(s[i])
            b.append(t[i])
        return sorted(s1)==sorted(s2)