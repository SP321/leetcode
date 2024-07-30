class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=s.count('a')
        b=0
        ans=a
        for x in s:
            if x=='b':
                b+=1
            else:
                a-=1
            ans=min(ans,a+b)
        return ans