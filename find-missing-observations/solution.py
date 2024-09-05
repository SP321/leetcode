class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        x=(n+m)*mean-sum(rolls)
        q,r=divmod(x,n)
        if q<=0 or q+(r>0)>6:
            return []
        return [q+(i<r) for i in range(n)]
            
