class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        x=[(i.count('0'),i.count('1')) for i in strs]
        nn=len(x)
        @cache
        def dfs(i,zeroes,ones):
            if zeroes<0 or ones<0:
                return float('-inf')
            if i==nn:
                return 0
            a,b=x[i]
            return max(
                dfs(i+1,zeroes,ones),
                dfs(i+1,zeroes-a,ones-b)+1
            )
        return dfs(0,m,n)