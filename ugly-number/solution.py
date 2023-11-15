class Solution:
    def isUgly(self, n: int) -> bool:
        for i in [5,3,2]:
            while n>0 and n%i==0:
                n//=i
        return n==1