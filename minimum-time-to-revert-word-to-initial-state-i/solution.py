def zf(s):
    n = len(s)
    z = [0] * n
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
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        z=zf(word)
        n=len(word)
        possible_pos=[]
        ans=(n+k-1)//k
        for i in range(n):
            if n-i==z[i]:
                possible_pos.append(i)
        possible_pos.append(n)
        for x in possible_pos:
            if x%k==0:
                 return x//k
        return ans