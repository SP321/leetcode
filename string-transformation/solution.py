M = 2**61 - 1
B  = 9973
def code(x): return ord(x) - ord('a') + 1
class HashedString:
    def __init__(self,s) -> None:
        n = len(s)
        self.ppow =  [1]
        self.hashes = [0]
        for i in range(n): self.ppow.append((self.ppow[-1]*B)%M)
        for i in range(n): self.hashes.append((self.hashes[-1]*B + code(s[i]))%M)
    def get_hash(self,i,j):
        return (self.hashes[j+1]-self.hashes[i]*self.ppow[j-i+1])%M
    

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        S = HashedString(s+s)
        T = HashedString(t)
        mod = 10**9 + 7
        nn = len(t)-1
        dp = [0,1]
        if k>1:
            inv = pow(nn+1,mod-2,mod)
            dp[0] = (pow(nn,k,mod) +  (1 if k%2==0 else -1)*nn)%mod
            dp[1] = (dp[0]+( (-1 if k%2==0 else 1)*(nn+1)) +mod)%mod
            dp[0] = (dp[0]*inv)%mod
            dp[1] = (dp[1]*inv)%mod
        ans = 0
        for i in range(len(s)):
            if S.get_hash(i,i+len(t)-1)==T.get_hash(0,len(t)-1):
                ans = (ans+dp[i>0])%mod
        return ans