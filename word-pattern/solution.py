class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split()
        if len(a)!=len(pattern):
            return False
        d,d2={},{}
        for x,y in zip(pattern,a):
            if x not in d:
                d[x]=y
            if y not in d2:
                d2[y]=x
            if d[x]!=y or d2[y]!=x:
                return False
        return True
