class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x=set(s)
        y=set(t)
        xy=set(zip(s,t))
        return len(x)==len(y)==len(xy)