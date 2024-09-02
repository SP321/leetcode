class Solution:
    def similarPairs(self, words: List[str]) -> int:
        c=Counter()
        ans=0
        for x in words:
            y=tuple(sorted(set(x)))
            ans+=c[y]
            c[y]+=1
        return ans