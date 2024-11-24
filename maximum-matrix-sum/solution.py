class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        c=0
        ans=0
        mn=inf
        for row in matrix:
            for x in row:
                ans+=abs(x)
                mn=min(mn,abs(x))
                c+=x<0
        if c%2==1:
            ans-=mn*2
        return ans
