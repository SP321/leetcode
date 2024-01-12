class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i,j=0,len(s)-1
        ans=0
        v=set('aeiouAEIOU')
        while i<j:
            if s[i] in v:
                ans+=1
            if s[j] in v:
                ans-=1
            i+=1
            j-=1
        return ans==0