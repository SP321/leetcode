class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        x=set(list(range(1,k+1)))
        for i in range(1,(k+1)//2):
            x.discard(k-i)
        for i in range(k+1,k+n-len(x)+1):
            x.add(i)
        return sum(list(x)[:n])
        