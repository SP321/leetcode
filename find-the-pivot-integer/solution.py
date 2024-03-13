class Solution:
    def pivotInteger(self, n: int) -> int:
        ans=((n*n+n)/2)**0.5
        return int(ans) if ans==int(ans) else -1
