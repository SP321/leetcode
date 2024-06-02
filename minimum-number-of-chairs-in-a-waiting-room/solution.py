class Solution:
    def minimumChairs(self, s: str) -> int:
        c=0
        ans=0
        for x in s:
            if x=='E':
                c+=1
                ans=max(ans,c)
            else:
                c-=1
        return ans