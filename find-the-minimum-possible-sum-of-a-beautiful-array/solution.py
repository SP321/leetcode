class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        ans=set()
        i=1
        while len(ans)!=n:
            off=target-i
            if off not in ans:
                ans.add(i)
            i+=1
        return sum(ans)
        