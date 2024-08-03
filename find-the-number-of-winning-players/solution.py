class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        a=[Counter() for _ in range(n)]
        for x,y in pick:
            a[x][y]+=1
        ans=0
        for i,x in enumerate(a):
            if max(list(x.values())+[0])>i:
                ans+=1
        return ans
