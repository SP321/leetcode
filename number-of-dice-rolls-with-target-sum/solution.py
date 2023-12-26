class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @cache
        def solve(target,dices):
            if(target == 0 and dices == 0):
                return 1
            if(target == 0):
                return 0
            if(dices < 1):
                return 0
            ans = 0
            for i in range(1,k+1):
                if(target >= i):
                    ans += solve(target-i,dices-1)
            return ans
        return solve(target,n) % (7 + 10**9)