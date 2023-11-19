class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        lx=-1
        for i in range(min(len(s) for s in [s1,s2,s3])):
            if s1[i]!=s2[i] or s2[i]!=s3[i]:
                break
            lx=i
        if lx==-1:
            return -1
        return sum(max(0,len(s)-(lx+1)) for s in [s1,s2,s3])

        