class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n>1:
            s.add(n)
            b=0
            while n>0:
                b+=(n%10)**2
                n//=10
            if b in s:
                return False
            n=b
        return True