class Solution:
    def minimumPushes(self, word: str) -> int:
        c=Counter(word)
        a=list(c.values())
        a.sort(reverse=True)
        ans=0
        for i in range(len(a)):
            ans+=a[i]*((i//8) +1)
        return ans