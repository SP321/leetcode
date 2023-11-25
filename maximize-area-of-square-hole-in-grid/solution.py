class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def helper(x):
            c=1
            ans=1
            x.sort()
            for i in range(1,len(x)):
                if x[i]==x[i-1]+1:
                    c+=1
                else:
                    c=1
                ans=max(ans,c)
            return ans
        ans=min(helper(hBars),helper(vBars))
        return (ans+1)**2
        