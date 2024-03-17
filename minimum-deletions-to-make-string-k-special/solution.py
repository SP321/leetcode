class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c=Counter(word)
        a=sorted(c.values(),reverse=True)
        n=len(word)
        ans=n
        i=0
        cur=0
        for j,x in enumerate(a):
            cur+=x
            while i<j and a[i]>x+k:
                cur-=a[i]
                i+=1
            ans=min(ans,n- (cur+i*(x+k)) )
        return ans