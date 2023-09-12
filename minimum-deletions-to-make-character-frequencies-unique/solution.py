class Solution:
    def minDeletions(self, s: str) -> int:
        x=list(Counter(s).values())
        x.sort(reverse=True)
        limit=x[0]
        ans=0
        for i in x[1:]:
            if i>=limit:
                ans+=i-(limit-1)
                limit=max(1,limit-1)
            else:
                limit=i
        return ans
                