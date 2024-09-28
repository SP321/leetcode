def zf(s):
    n = len(s)
    z = [0] * n
    z[0]=len(s)
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(z[i-l], r - i)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z

class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        aa=pattern+'$'+s
        a=zf(aa)
        bb=pattern[::-1]+'$'+s[::-1]
        b=zf(bb)
        n=len(s)
        
        for i in range(n):
            j=len(s)-1-(i+len(pattern)-1)
            if not 0<=j<n:
                break
            l=i+len(pattern)+1
            r=j+len(pattern)+1
            if a[l]+b[r]>=len(pattern)-1:
                return i

        return -1
