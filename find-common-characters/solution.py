class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c=defaultdict(lambda:inf)
        for x in ascii_lowercase:
            for w in words:
                c[x]=min(c[x],w.count(x))
        ans=[]
        for x in c:
            if c[x]>0:
                ans.extend([x]*c[x])
        return ans