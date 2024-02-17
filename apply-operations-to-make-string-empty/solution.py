class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        c=Counter(s)
        x=max(c.values())
        ans=[]
        c2=Counter()
        for i in s:
            c2[i]+=1
            if c2[i]==x:
                ans.append(i)
        return ''.join(ans)