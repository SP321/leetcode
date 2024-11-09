class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        ans=n
        while prod(map(int,str(ans)))%t!=0:
            ans+=1
        return ans