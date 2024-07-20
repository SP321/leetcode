class Solution:
    def minimumLength(self, s: str) -> int:
        c=Counter(s)
        ans=0
        for x in c.values():
            ans+=2 if x%2==0 else 1
        return ans