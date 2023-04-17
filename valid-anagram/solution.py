class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counts(s):
            x={}
            for i in s:
                if i in x:
                    x[i]+=1
                else:
                    x[i]=1
            return x
        return counts(s)==counts(t)