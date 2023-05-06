class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x={}
        y=set()
        for i in range(len(s)):
            if s[i] not in x:
                if t[i] not in y:
                    y.add(t[i])
                else:
                    return False
                x[s[i]]=t[i]
            if x[s[i]]!=t[i]:
                return False
        return True