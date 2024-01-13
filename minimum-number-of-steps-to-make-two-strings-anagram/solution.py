class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c=Counter(s)
        for i in t:
            if i in c:
                c[i]-=1
                if c[i]==0:
                    del c[i]
        return sum(c.values())