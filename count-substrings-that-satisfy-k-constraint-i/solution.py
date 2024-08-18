class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        i=0
        c=0
        c1=0
        for j in range(n):
            c+=1-int(s[j])
            c1+=int(s[j])
            while c>k and c1>k:
                c-=1-int(s[i])
                c1-=int(s[i])
                i+=1
            if c<=k or c1<=k:
                ans+=j-i+1
        return ans
