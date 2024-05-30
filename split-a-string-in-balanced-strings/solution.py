class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        c=0
        for x in s:
            if x=='L':
                c+=1
            else:
                c-=1
            ans+=c==0
        return ans