class Solution:
    def canAliceWin(self, n: int) -> bool:
        take=10
        alice=True
        while n>=take and take!=0:
            n-=take
            alice=not alice
            take-=1
        return not alice
            