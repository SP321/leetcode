class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        for i in s:
            k=t[j:].find(i)
            if k==-1:
                return False
            j+=k+1
        return True