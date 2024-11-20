class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n=len(s)
        c = [0] * 3
        for x in s:
            c[ord(x)%32-1]+=1
        i=0 
        if min(c)<k:
            return -1
        ans=0
        for j in range(n):
            val=ord(s[j])%32-1
            c[val]-=1
            while i<=j and c[val]<k:
                val2=ord(s[i])%32-1
                c[val2]+=1
                i+=1
            ans=max(ans,j-i+1)
        return n-ans