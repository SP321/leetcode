class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        c=[0]*n
        for i in range(n):
            c[i]= len(set(A[:i+1]).intersection(set(B[:i+1])))
        return c
        