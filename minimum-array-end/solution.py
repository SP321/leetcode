class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n-=1
        ans=x
        pos=0
        while n:
            while ans&(1<<pos):
                pos+=1
            if n&1:
                ans|=1<<pos
            pos+=1
            n>>=1
        return ans